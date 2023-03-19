from django_filters import FilterSet
from oms.models import SkuList


class SkuListFilter(FilterSet):
    class Meta:
        model = SkuList
        # fields = ('tm_order_id',) #这个是元组，因此如果只有一个的话，记得在最后面加上逗号
        fields = ('tm_order_id', 'tm_order_create_time', 'tm_order_confirm_time')
