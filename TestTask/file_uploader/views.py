from rest_framework import status
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework.views import APIView

from file_uploader.models import UploadFile

from file_uploader.serializers import UploaderSerializer


class Uploader(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]

    def post(self, request):
        file = UploadFile.objects.create(owner=self.request.user, file=request.data.get('datafile'))
        return Response(data=UploaderSerializer(file).data, status=status.HTTP_201_CREATED)

    def get(self, request):
        files = UploadFile.objects.all()
        print(files)
        return Response(status=status.HTTP_200_OK)
