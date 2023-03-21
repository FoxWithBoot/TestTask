from rest_framework import status
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework.views import APIView

from file_uploader.models import UploadFile, User

from file_uploader.serializers import UploaderSerializer, FileListSerializer

import pandas as pd


class Uploader(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]

    def post(self, request):
        file = UploadFile.objects.create(owner=self.request.user, file=request.data.get('datafile'))
        return Response(data=UploaderSerializer(file).data, status=status.HTTP_201_CREATED)

    def get(self, request):
        files = UploadFile.objects.all()
        files_list = []
        for f in files:
            data = pd.read_csv(f.file.name)
            serialized_file = UploaderSerializer(f).data
            serialized_file['fields'] = list(data.columns)
            files_list.append(serialized_file)
        return Response(data=files_list, status=status.HTTP_200_OK)

    # def get(self, request):
    #     files = UploadFile.objects.all()
    #     files_list = []
    #     for f in files:
    #         data = pd.read_csv(f.file.name)
    #         files_list.append({'file': f, 'fields': list(data.columns)})
    #     return Response(data=FileListSerializer(files_list, many=True).data, status=status.HTTP_200_OK)