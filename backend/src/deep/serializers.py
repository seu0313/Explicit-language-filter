from rest_framework import serializers
from deep.models import Deep

# FileUpload Parser
class DeepSerializer(serializers.ModelSerializer):
    class Meta:
        model = Deep
        fields = ('id', 'title', 'video_file')