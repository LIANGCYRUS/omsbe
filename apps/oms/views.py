from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from oms.models import SkuList
from oms.serializer import SkuListSerializer


# Create your views here.
class SkuListViewSet(ModelViewSet):
    queryset = SkuList.objects.all()
    serializer_class = SkuListSerializer