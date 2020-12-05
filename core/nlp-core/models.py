from keras.models import Model
from keras.layers import Input, Embedding, Conv1D, BatchNormalization, Activation, Add
from keras.layers import MaxPooling1D, Dense, Flatten, Dropout

from keras.engine.topology import get_source_inputs
from k_max_pooling import KMaxPooling, KMaxPoolingNotSorted

# CharCNN 모델
class CharCNN:
    def __init__(self):
        pass

    def create_model(self, input_size, embedding_layer, conv_layers, fully_connected_layers, dropout_point, num_of_classes):
        # Input
        inputs = Input(shape=(input_size,), name='input', dtype='int64')  # shape=(?, 1014)
        # Embedding
        x = embedding_layer(inputs)
        # Conv
        for filter_num, filter_size, pooling_size in conv_layers:
            x = Conv1D(filter_num, filter_size)(x)
            x = Activation('relu')(x)
            if pooling_size != -1:
                x = MaxPooling1D(pool_size=pooling_size)(x)  # Final shape=(None, 34, 256)
        x = Flatten()(x)  # (None, 8704)
        # Fully connected layers
        for dense_size in fully_connected_layers:
            x = Dense(dense_size, activation='relu')(x)  # dense_size == 1024
            x = Dropout(dropout_point)(x)
        # Output Layer
        predictions = Dense(num_of_classes, activation='softmax')(x)
        # Build model
        model = Model(inputs=inputs, outputs=predictions)

        return model


# VDCNN 모델
class VDCNN:
    def __init__(self):
        pass

    def base_block(self, inputs, filters, kernel_size=3, use_bias=False, shortcut=False):
        conv_1 = Conv1D(filters=filters, kernel_size=kernel_size, strides=1, padding='same')(inputs)
        batch_norm_1 = BatchNormalization()(conv_1)
        activate_relu = Activation('relu')(batch_norm_1)
        conv_2 = Conv1D(filters=filters, kernel_size=kernel_size, strides=1, padding='same')(activate_relu)
        output = BatchNormalization()(conv_2)

        if shortcut:
            output = Add()([output, inputs])
        output = Activation('relu')(output)

        return output

    def conv_block(self, inputs, filters, kernel_size=3, use_bias=False, shortcut=False, pool_type='max', sorted=True):
        conv_1 = Conv1D(filters=filters, kernel_size=kernel_size, strides=1, padding='same')(inputs)
        batch_norm_1 = BatchNormalization()(conv_1)
        activate_relu = Activation('relu')(batch_norm_1)
        conv_2 = Conv1D(filters=filters, kernel_size=kernel_size, strides=1, padding='same')(activate_relu)
        batch_norm_2 = BatchNormalization()(conv_2)

        if shortcut:
            # shortcut Conv1D 작업 및 배치 정규화
            shortcut_conv = Conv1D(filters=filters, kernel_size=1, strides=2)(inputs)
            shortcut_batch_norm = BatchNormalization()(shortcut_conv)
            
            # Case. max_pooling 하는 경우, k-max pooling 하는 경우 등.
            output = self.down_sample(batch_norm_2, pool_type=pool_type, sorted=sorted)
            output = Add()([output, shortcut_batch_norm])
            output = Activation('relu')(output)
        else:  # 마지막 k-max을 진행하는 경우 shortcut을 하지 않고 k-max pooling 진행
            output = Activation('relu')(batch_norm_2)
            output = self.down_sample(output, pool_type=pool_type, sorted=sorted)

        if pool_type is not None:
            output = Conv1D(filters=2*filters, kernel_size=1, strides=1, padding='same')(output)
            output = BatchNormalization()(output)

        return output

    def down_sample(self, inputs, pool_type='max', sorted=True):
        if pool_type == 'max':
            output = MaxPooling1D(pool_size=3, strides=2, padding='same')(inputs)
        elif pool_type == 'k_max':
            k = int(inputs._keras_shape[1]/2)
            output = KMaxPooling(k=k, sorted=sorted)(inputs)
        elif pool_type == 'conv':
            output = Conv1D(filters=inputs._keras_shape[-1], kernel_size=3, strides=2, padding='same')(inputs)
            output = BatchNormalization()(output)
        elif pool_type is None:
            output = inputs
        else:
            raise ValueError('지원하지 않는 풀링 타입')

        return output

    def create_model(self, num_of_classes, sequence_length=1024, embedding_dim=16, shortcut=False, pool_type='max', sorted=True, use_bias=False, input_tensor=None):
        num_conv_blocks = (1, 1, 1, 1)  # depth 9
        # num_conv_blocks = (2, 2, 2, 2)  # depth 17
        # num_conv_blocks = (5, 5, 2, 2)  # depth 29
        # num_conv_blocks = (8, 8, 5, 3)  # depth 49

        inputs = Input(shape=(sequence_length, ))
        embedded_chars = Embedding(input_dim=sequence_length, output_dim=embedding_dim)(inputs)

        # temp convolution
        output = Conv1D(filters=64, kernel_size=3, strides=1, padding='same')(embedded_chars)

        # Convolutional Block 64
        for _ in range(num_conv_blocks[0] - 1):
            output = self.base_block(output, filters=64, kernel_size=3, use_bias=use_bias, shortcut=shortcut)
        output = self.conv_block(output, filters=64, kernel_size=3, use_bias=use_bias, shortcut=shortcut, pool_type=pool_type, sorted=sorted)

        # Convolutional Block 128
        for _ in range(num_conv_blocks[1] - 1):
            output = self.base_block(output, filters=128, kernel_size=3, use_bias=use_bias, shortcut=shortcut)
        output = self.conv_block(output, filters=128, kernel_size=3, use_bias=use_bias, shortcut=shortcut, pool_type=pool_type, sorted=sorted)

        # Convolutional Block 256
        for _ in range(num_conv_blocks[2] - 1):
            output = self.base_block(output, filters=256, kernel_size=3, use_bias=use_bias, shortcut=shortcut)
        output = self.conv_block(output, filters=256, kernel_size=3, use_bias=use_bias, shortcut=shortcut, pool_type=pool_type, sorted=sorted)

        # Convolutional Block 512
        for _ in range(num_conv_blocks[3] - 1):
            output = self.base_block(output, filters=512, kernel_size=3, use_bias=use_bias, shortcut=shortcut)
        output = self.conv_block(output, filters=512, kernel_size=3, use_bias=use_bias, shortcut=False, pool_type=None)

        # K-max pooling (k=8)
        output = KMaxPooling(k=8, sorted=True)(output)
        output = Flatten()(output)

        # Dense Layers
        output = Dense(2048, activation='relu')(output)
        output = Dense(2048, activation='relu')(output)
        output = Dense(num_of_classes, activation='softmax')(output)

        if input_tensor is not None:
            inputs = get_source_inputs(input_tensor)
        else:
            inputs = inputs

        # Model 생성
        model = Model(inputs=inputs, outputs=output)

        return model

if __name__ == "__main__":
    vdcnn = VDCNN()
    model = vdcnn.create_model(10, shortcut=False, pool_type='max')
    model.summary()