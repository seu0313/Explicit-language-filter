from keras.callbacks import ModelCheckpoint, EarlyStopping
from keras.models import Model, load_model, Sequential
from keras.layers import Dense, Activation, Dropout, Input, Masking, Add, TimeDistributed
from keras.layers import Conv1D, BatchNormalization, Reshape, MaxPooling1D, Embedding
from keras.optimizers import Adam, SGD, RMSprop

from keras.engine import Layer, InputSpec
from keras.layers import Flatten
import tensorflow as tf

class KMaxPooling(Layer):
    """
    K-max pooling layer that extracts the k-highest activations from a sequence (2nd dimension).
    TensorFlow backend.
    """
    def __init__(self, k=1, **kwargs):
        super().__init__(**kwargs)
        self.input_spec = InputSpec(ndim=3)
        self.k = k

    def compute_output_shape(self, input_shape):
        return (input_shape[0], (input_shape[2] * self.k))

    def call(self, inputs):
        
        # swap last two dimensions since top_k will be applied along the last dimension
        shifted_input = tf.transpose(inputs, [0, 2, 1])
        
        # extract top_k, returns two tensors [values, indices]
        top_k = tf.nn.top_k(shifted_input, k=self.k, sorted=True, name=None)[0]
        
        # return flattened output
        return Flatten()(top_k)

def CharCNN_model(input_shape):
    '''
        charCNN을 활용한 모델
        input_shape: 입력 자모 데이터
        
        return: 설계된 모델을 반환함
    '''

    X_input = Input(shape=input_shape)

    X = None

    model = Model(input_shape=X_input, outputs=X)

    return model


def VDCNN_model(input_shape):
    '''
        ## 아직 미완성 (오류 많음)
        charCNN을 매우 깊게 적용한 모델
        input_shape: 입력 자모 데이터
        
        return: 설계된 모델을 반환함
    '''

    # Parameters
    # input_size = len(input_shape)
    input_size = 1024
    vocab_size = 69
    embedding_size = 69
    conv_layer = [
        [64, 7, 3],
        [128, 7, 3],
        [256, 3, 3],
        [512, 3, 3]
    ]

    fully_connected_layers = [1024, 1024]
    num_of_classes = 4
    dropout_point = 0.5

    # 입력
    embedding_layer = Embedding(vocab_size+1, embedding_size, input_length=input_size)

    X_input = Input(shape = input_shape)
    X = embedding_layer(X_input)

    # Conv layer
    cnt = 0
    for filter_num, filter_size, stride_size in conv_layer:
        Y = Conv1D(filter_num, kernel_size=filter_size, strides=stride_size)(X)
        Y = BatchNormalization()(Y)
        Y = Activation('relu')(Y)

        Y = Conv1D(filter_num, kernel_size=filter_size, strides=stride_size)(Y)
        Y = BatchNormalization()(Y)
        Y = Activation('relu')(Y)

        X = Add()([X, Y])  # short connection

        Y = Conv1D(filter_num, kernel_size=filter_size, strides=stride_size)(X)
        Y = BatchNormalization()(Y)
        Y = Activation('relu')(Y)

        Y = Conv1D(filter_num, kernel_size=filter_size, strides=stride_size)(Y)
        Y = BatchNormalization()(Y)
        Y = Activation('relu')(Y)

        if cnt != len(conv_layer)-1:
            # Y = MaxPooling1D(pool_size=2, strides=2)
            X = Add()([X, Y])  # short connection
        cnt += 1
    
    X = Flatten()(Y)

    # k-max pooling (k=8)
    X = KMaxPooling(k=8)(X)

    # Fully connected layers
    for dense_size in fully_connected_layers:
        X = Dense(dense_size, activation='relu')(X)
        X = Dropout(dropout_point)(X)

    # Output layer
    X_output = Dense(num_of_classes, activation='softmax')

    '''
    # 레이어
    X = Conv1D(64, kernel_size=16, stride=1)(X_input)

    # Convolution block I
    Y = Conv1D(64, kernel_size=1, stride=1)(X)
    Y = BatchNormalization()(Y)
    Y = Dense(1, activation='relu')

    Y = Conv1D(64, kernel_size=1, stride=1)(Y)
    Y = BatchNormalization()(Y)
    Y = Dense(1, activation='relu')

    X = Add()([X, Y])  # short connection

    Y = Conv1D(64, kernel_size=1, stride=1)(X)
    Y = BatchNormalization()(Y)
    Y = Dense(1, activation='relu')

    Y = Conv1D(64, kernel_size=1, stride=1)(Y)
    Y = BatchNormalization()(Y)
    Y = Dense(1, activation='relu')

    # Pooling /2
    Y = MaxPooling1D(pool_size=64//2)

    X = Add()([X, Y])  # short connection

    # Convolution block II
    Y = Conv1D(128, kernel_size=1, stride=1)(X)
    Y = BatchNormalization()(Y)
    Y = Dense(1, activation='relu')

    Y = Conv1D(128, kernel_size=1, stride=1)(Y)
    Y = BatchNormalization()(Y)
    Y = Dense(1, activation='relu')

    X = Add()([X, Y])  # short connection

    Y = Conv1D(128, kernel_size=1, stride=1)(X)
    Y = BatchNormalization()(Y)
    Y = Dense(1, activation='relu')

    Y = Conv1D(128, kernel_size=1, stride=1)(Y)
    Y = BatchNormalization()(Y)
    Y = Dense(1, activation='relu')

    # Pooling /2
    Y = MaxPooling1D(pool_size=64//2)

    X = Add()([X, Y])  # short connection

    # Convolution block III
    Y = Conv1D(256, kernel_size=1, stride=1)(X)
    Y = BatchNormalization()(Y)
    Y = Dense(1, activation='relu')

    Y = Conv1D(256, kernel_size=1, stride=1)(Y)
    Y = BatchNormalization()(Y)
    Y = Dense(1, activation='relu')

    X = Add()([X, Y])  # short connection

    Y = Conv1D(256, kernel_size=1, stride=1)(X)
    Y = BatchNormalization()(Y)
    Y = Dense(1, activation='relu')

    Y = Conv1D(256, kernel_size=1, stride=1)(Y)
    Y = BatchNormalization()(Y)
    Y = Dense(1, activation='relu')

    # Pooling /2
    Y = MaxPooling1D(pool_size=64//2)

    X = Add()([X, Y])  # short connection

    # Convolution block IV
    Y = Conv1D(512, kernel_size=1, stride=1)(X)
    Y = BatchNormalization()(Y)
    Y = Dense(1, activation='relu')

    Y = Conv1D(512, kernel_size=1, stride=1)(Y)
    Y = BatchNormalization()(Y)
    Y = Dense(1, activation='relu')

    X = Add()([X, Y])  # short connection

    X = Conv1D(512, kernel_size=1, stride=1)(X)
    X = BatchNormalization()(X)
    X = Dense(1, activation='relu')

    X = Conv1D(512, kernel_size=1, stride=1)(X)
    X = BatchNormalization()(X)
    X = Dense(1, activation='relu')

    # k-max pooling (k=8)
    X = KMaxPooling(k=8)(X)

    # FC
    X = Dense((4096, 2048), activation='relu')
    X = Dense((2048, 2048), activation='relu')
    
    n = None # 임시
    X = TimeDistributed(Dense(n, activation = "softmax"))(X)
    '''

    # 생성
    model = Model(inputs = X_input, outputs = X_output)


    return model



import keras
from keras.models import Model
from keras.layers import Input, Embedding, Conv1D, BatchNormalization, Activation, Add, MaxPooling1D, Dense, Flatten
from keras.engine.topology import get_source_inputs

from keras.engine import Layer, InputSpec
from keras.layers import Flatten
import tensorflow as tf


class KMaxPooling_(Layer):
    """
    K-max pooling layer that extracts the k-highest activations from a sequence (2nd dimension).
    TensorFlow backend.
    """
    def __init__(self, k=1, sorted=True, **kwargs):
        super().__init__(**kwargs)
        self.input_spec = InputSpec(ndim=3)
        self.k = k
        self.sorted = sorted

    def compute_output_shape(self, input_shape):
        return (input_shape[0], self.k, input_shape[2])

    def call(self, inputs):
        # swap last two dimensions since top_k will be applied along the last dimension
        shifted_inputs = tf.transpose(inputs, [0, 2, 1])
        
        # extract top_k, returns two tensors [values, indices]
        top_k = tf.nn.top_k(shifted_inputs, k=self.k, sorted=self.sorted)[0]
        
        # return flattened output
        return tf.transpose(top_k, [0,2,1])



def identity_block(inputs, filters, kernel_size=3, use_bias=False, shortcut=False):
    conv1 = Conv1D(filters=filters, kernel_size=kernel_size, strides=1, padding='same')(inputs)
    bn1 = BatchNormalization()(conv1)
    relu = Activation('relu')(bn1)
    conv2 = Conv1D(filters=filters, kernel_size=kernel_size, strides=1, padding='same')(relu)
    out = BatchNormalization()(conv2)
    if shortcut:
        out = Add()([out, inputs])
    return Activation('relu')(out)

def conv_block(inputs, filters, kernel_size=3, use_bias=False, shortcut=False, 
               pool_type='max', sorted=True, stage=1):
    conv1 = Conv1D(filters=filters, kernel_size=kernel_size, strides=1, padding='same')(inputs)
    bn1 = BatchNormalization()(conv1)
    relu1 = Activation('relu')(bn1)

    conv2 = Conv1D(filters=filters, kernel_size=kernel_size, strides=1, padding='same')(relu1)
    out = BatchNormalization()(conv2)

    if shortcut:
        residual = Conv1D(filters=filters, kernel_size=1, strides=2, name='shortcut_conv1d_%d' % stage)(inputs)
        residual = BatchNormalization(name='shortcut_batch_normalization_%d' % stage)(residual)
        out = downsample(out, pool_type=pool_type, sorted=sorted, stage=stage)
        out = Add()([out, residual])
        out = Activation('relu')(out)
    else:
        out = Activation('relu')(out)
        out = downsample(out, pool_type=pool_type, sorted=sorted, stage=stage)
    if pool_type is not None:
        out = Conv1D(filters=2*filters, kernel_size=1, strides=1, padding='same', name='1_1_conv_%d' % stage)(out)
        out = BatchNormalization(name='1_1_batch_normalization_%d' % stage)(out)
    return out

def downsample(inputs, pool_type='max', sorted=True, stage=1):
    if pool_type == 'max':
        out = MaxPooling1D(pool_size=3, strides=2, padding='same', name='pool_%d' % stage)(inputs)
    elif pool_type == 'k_max':
        k = int(inputs._keras_shape[1]/2)
        out = KMaxPooling(k=k, sorted=sorted, name='pool_%d' % stage)(inputs)
    elif pool_type == 'conv':
        out = Conv1D(filters=inputs._keras_shape[-1], kernel_size=3, strides=2, padding='same', name='pool_%d' % stage)(inputs)
        out = BatchNormalization()(out)
    elif pool_type is None:
        out = inputs
    else:
        raise ValueError('unsupported pooling type!')
    return out

def VDCNN(num_classes, depth=9, sequence_length=1024, embedding_dim=16, 
          shortcut=False, pool_type='max', sorted=True, use_bias=False, input_tensor=None):
    if depth == 9:
        num_conv_blocks = (1, 1, 1, 1)
    elif depth == 17:
        num_conv_blocks = (2, 2, 2, 2)
    elif depth == 29:
        num_conv_blocks = (5, 5, 2, 2)
    elif depth == 49:
        num_conv_blocks = (8, 8, 5, 3)
    else:
        raise ValueError('unsupported depth for VDCNN.')

    inputs = Input(shape=(sequence_length, ), name='inputs')
    embedded_chars = Embedding(input_dim=sequence_length, output_dim=embedding_dim)(inputs)
    out = Conv1D(filters=64, kernel_size=3, strides=1, padding='same', name='temp_conv')(embedded_chars)

    # Convolutional Block 64
    for _ in range(num_conv_blocks[0] - 1):
        out = identity_block(out, filters=64, kernel_size=3, use_bias=use_bias, shortcut=shortcut)
    out = conv_block(out, filters=64, kernel_size=3, use_bias=use_bias, shortcut=shortcut, 
                     pool_type=pool_type, sorted=sorted, stage=1)

    # Convolutional Block 128
    for _ in range(num_conv_blocks[1] - 1):
        out = identity_block(out, filters=128, kernel_size=3, use_bias=use_bias, shortcut=shortcut)
    out = conv_block(out, filters=128, kernel_size=3, use_bias=use_bias, shortcut=shortcut, 
                     pool_type=pool_type, sorted=sorted, stage=2)

    # Convolutional Block 256
    for _ in range(num_conv_blocks[2] - 1):
        out = identity_block(out, filters=256, kernel_size=3, use_bias=use_bias, shortcut=shortcut)
    out = conv_block(out, filters=256, kernel_size=3, use_bias=use_bias, shortcut=shortcut, 
                     pool_type=pool_type, sorted=sorted, stage=3)

    # Convolutional Block 512
    for _ in range(num_conv_blocks[3] - 1):
        out = identity_block(out, filters=512, kernel_size=3, use_bias=use_bias, shortcut=shortcut)
    out = conv_block(out, filters=512, kernel_size=3, use_bias=use_bias, shortcut=False, 
                     pool_type=None, stage=4)

    # k-max pooling with k = 8
    out = KMaxPooling(k=8, sorted=True)(out)
    out = Flatten()(out)

    # Dense Layers
    out = Dense(2048, activation='relu')(out)
    out = Dense(2048, activation='relu')(out)
    out = Dense(num_classes, activation='softmax')(out)

    if input_tensor is not None:
        inputs = get_source_inputs(input_tensor)
    else:
        inputs = inputs

    # Create model.
    model = Model(inputs=inputs, outputs=out, name='VDCNN')
    return model

if __name__ == "__main__":
    model = VDCNN(10, depth=9, shortcut=False, pool_type='max')
    model.summary()
if __name__ == "__main__":

    optimizer = 'adam'
    loss = 'categorical_crossentropy'


    # model = VDCNN_model((1024,))
    model = CharCNN_model(input_shape=(5511, 101))
    model.compile(optimizer=optimizer, loss=loss, metrics=['accuracy'])
    model.summary()
    