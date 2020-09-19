from django.shortcuts import render
from rest_framework import viewsets, permissions, status
from rest_framework.parsers import FileUploadParser, ParseError
from rest_framework.response import Response
from deep.models import Deep
from deep.serializers import DeepSerializer


# Deep File
class DeepViewSet(viewsets.ModelViewSet):
    queryset = Deep.objects.all()
    serializer_class = DeepSerializer
    # parser_classes = (FileUploadParser, )
    permission_classes = [permissions.IsAuthenticated]