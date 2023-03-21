from rest_framework import serializers

from file_uploader.models import UploadFile


class UploaderSerializer(serializers.ModelSerializer):
    class Meta:
        model = UploadFile
        fields = ('created', 'datafile', 'owner')