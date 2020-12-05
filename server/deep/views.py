## src
import requests
import numpy as np

# Django
from django.shortcuts import render
from rest_framework import viewsets, permissions, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view, parser_classes

# Deep
from deep.models import Deep
from deep.serializers import DeepSerializer
from deep.feature.feat_nlp import processing_with_gcp
from deep.feature.feat_spec import processing_with_detection

# from deep.utils import processing_with_detection, processing_with_gcp

## code
class DeepViewSet(viewsets.ModelViewSet):
    queryset = Deep.objects.all()
    serializer_class = DeepSerializer

    def create(self, request):
        if request.method == 'POST':
            if request.data['choice_method'] == 'GCP':
                video_file = request.FILES['video_file']

                try:
                    video_file, durations = processing_with_gcp(video_file)
                    request.data['video_duration'] = durations
                    
                except Exception as err:
                    print(err)
                    print(f'비디오 처리 실패')
                
                serializer = DeepSerializer(data=request.data)
                if serializer.is_valid():
                    serializer.save()
                    return Response(serializer.data, status=status.HTTP_201_CREATED)
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            else:
                video_file = request.FILES['video_file']

                try:
                    video_file, durations = processing_with_detection(video_file)
                    request.data['video_duration'] = durations                    
                except Exception as err:
                    print(f'비디오 처리 실패: {err}')
                serializer = DeepSerializer(data=request.data)
                if serializer.is_valid():
                    serializer.save()
                    return Response(serializer.data, status=status.HTTP_201_CREATED)
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)