from django.shortcuts import get_object_or_404
from rest_framework.parsers import FileUploadParser
from rest_framework.response import Response 
from rest_framework.views import APIView
from rest_framework import status,filters
from django_filters import rest_framework
from .serializers import FileSerializer
from .models import UploadModel
from rest_framework.viewsets import ModelViewSet
from rest_framework import generics
from rest_framework.filters import SearchFilter


class UploadAPIView(generics.ListAPIView):
    print("FileUploadViewSet")
    queryset = UploadModel.objects.all()
    serializer_class = FileSerializer
    filter_backends = (filters.SearchFilter,)
    parser_classes = (FileUploadParser,)
    search_fields = ("name","id", "choice")
    # def get(self, request):
    #     obj = UploadModel.objects.all()
    #     data = FileSerializer(obj, many=True).data
    #     return Response(data)

class UploadDetailAPIView(APIView):
    
    def get(self, request, pk):
        obj = get_object_or_404(UploadModel, pk=pk)
        data = FileSerializer(obj).data
        return Response(data)


class FileUploadView(APIView):
    

    parser_class = (FileUploadParser, )

    def post(self, request, *args , **kwargs):
        file_serializer = FileSerializer(data=request.data)
        print(file_serializer)
        if file_serializer.is_valid():
            file_serializer.save()
            return Response(file_serializer.data, status=status.HTTP_201_CREATED)

        else:
            print("Serializweris not valid")
            return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)





