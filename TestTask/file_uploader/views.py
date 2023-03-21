from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from file_uploader.models import UploadFile


class Uploader(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request, format='csv'):
        f = request.data.get('datafile')
        ff = UploadFile.objects.create(owner=self.request.user, file=f)
        print(ff)
        return Response(status.HTTP_201_CREATED)
