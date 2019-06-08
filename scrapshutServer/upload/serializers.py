from rest_framework import serializers
from .models import UploadModel

class FileSerializer(serializers.ModelSerializer):

    class Meta:
        model = UploadModel
        fields = "__all__"