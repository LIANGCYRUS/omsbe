from rest_framework import serializers
from oms.models import SkuList


class SkuListSerializer(serializers.ModelSerializer):
    class Meta:
        model = SkuList
        fields = '__all__'
