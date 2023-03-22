from rest_framework import serializers

from file_uploader.models import UploadFile


class UploaderSerializer(serializers.ModelSerializer):
    class Meta:
        model = UploadFile
        fields = ('owner', 'created', 'file')


# class FileListSerializer(serializers.ModelSerializer):
#     #file = UploaderSerializer()
#     fields = serializers.ListField()
#
#     class Meta:
#         model = UploadFile
#         fields = ('owner', 'created', 'file', 'fields')
class FormalSerializer(serializers.ModelSerializer):
    fields = serializers.ListField()
    class Meta:
        model = UploadFile
        fields = ('owner', 'created', 'file', 'fields')

class FileListSerializer(serializers.Serializer):
    file = UploaderSerializer()
    fields = serializers.ListField()


class ErrorSerializer(serializers.Serializer):
    detail = serializers.CharField()
