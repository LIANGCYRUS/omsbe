from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from oms.models import SkuList
from oms.serializer import SkuListSerializer
from oms.filters import SkuListFilter
from rest_framework.filters import SearchFilter

from rest_framework.pagination import PageNumberPagination
from oms.paginations import MyPageNumberPaginations

# Create your views here.
class SkuListViewSet(ModelViewSet):
    queryset = SkuList.objects.all()
    serializer_class = SkuListSerializer

    pagination_class = MyPageNumberPaginations

    # filter_backends = (SearchFilter,)
    filter_class = SkuListFilter
    search_fields = ('tm_order_id','tm_order_sub_id','ali_id')

