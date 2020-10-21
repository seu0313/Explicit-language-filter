from django.shortcuts import render
from rest_framework import viewsets, permissions, status
from rest_framework.views import APIView
from rest_framework.parsers import FileUploadParser, ParseError, FormParser, MultiPartParser
from rest_framework.response import Response
from rest_framework.decorators import api_view, parser_classes
from deep.models import Deep
from deep.serializers import DeepSerializer
from .utils import video_processing

# Deep File
class DeepViewSet(viewsets.ModelViewSet):
    queryset = Deep.objects.all()
    serializer_class = DeepSerializer
    # parser_classes = (FileUploadParser, )
    # permission_classes = [permissions.IsAuthenticated]

# FBV
@api_view(['GET','POST'])
def Deep_list(request):
    if request.method == 'GET':
        queryset = Deep.objects.all()
        serializer = DeepSerializer(queryset, many=True)
        return Response(serializer.data)
    else:
        video_file = request.data['video_file']
        try:
            video_file = video_processing(video_file)
        except:
            pass
        serializer = DeepSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            print(f"데이터 {serializer.data['video_file']}")
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)