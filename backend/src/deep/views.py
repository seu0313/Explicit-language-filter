from django.shortcuts import render
from rest_framework import viewsets, permissions, status
from rest_framework.views import APIView
from rest_framework.parsers import FileUploadParser, ParseError, FormParser, MultiPartParser
from rest_framework.response import Response
from deep.models import Deep
from deep.serializers import DeepSerializer


# Deep File
class DeepViewSet(viewsets.ModelViewSet):
    queryset = Deep.objects.all()
    serializer_class = DeepSerializer
    # parser_classes = (FileUploadParser, )
    # permission_classes = [permissions.IsAuthenticated]

# class DeepView(APIView):
#     parser_classes = (MultiPartParser, FormParser)

#     def get(self, request, *args, **kwargs):
#         Deeps = Deep.objects.all()
#         serializer = DeepSerializer(Deeps, many=True)
#         return Response(serializer.data)

#     def post(self, request, *args, **kwargs):
#         Deeps_serializer = DeepSerializer(data=request.data)
#         if Deeps_serializer.is_valid():
#             Deeps_serializer.save()
#             return Response(Deeps_serializer.data, status=status.HTTP_201_CREATED)
#         else:
#             print('error', Deeps_serializer.errors)
#             return Response(Deeps_serializer.errors, status=status.HTTP_400_BAD_REQUEST)