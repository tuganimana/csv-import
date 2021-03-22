from rest_framework import serializers
from .models import *
class UploadcsvSerializers(serializers.ModelSerializer):

    class Meta:
        model=Uploadcsv
        fields=('__all__')