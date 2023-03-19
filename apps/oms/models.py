from django.db import models

# Create your models here.


# ===== 合并订单 =====

class SkuList(models.Model):
    tm_order_id=models.CharField(verbose_name='主订单编号', max_length=100, null=True, blank=True)
    tm_order_sub_id=models.CharField(verbose_name='子订单编号', max_length=100, null=True, blank=True)
    tm_sku_name = models.CharField(verbose_name='标题', max_length=100, null=True, blank=True)
    numm = models.CharField(verbose_name='购买数量', max_length=100, null=True, blank=True)
    option = models.CharField(verbose_name='商品属性', max_length=100, null=True, blank=True)
    buy_sku_name=models.CharField(verbose_name='入货品', max_length=100, null=True, blank=True)
    sku_cost_price = models.IntegerField(verbose_name='入货价', max_length=100, null=True, blank=True)
    customer_paid = models.CharField(verbose_name='买家应付货款', max_length=100, null=True, blank=True)
    tm_order_create_time = models.DateTimeField(verbose_name='订单创建时间_x', max_length=100, null=True, blank=True)
    tm_order_payment_time = models.DateTimeField(verbose_name='订单付款时间', max_length=100, null=True, blank=True)
    ali_order_id = models.CharField(verbose_name='Partner_transaction_id', max_length=100, null=True, blank=True)
    ali_id=models.CharField(verbose_name='Transaction_id', max_length=100, null=True, blank=True)
    ali_usd_amount = models.FloatField(verbose_name='Amount', max_length=100, null=True, blank=True)
    ali_cny_amount = models.CharField(verbose_name='Rmb_amount', max_length=100, null=True, blank=True)
    ali_usd_fee = models.FloatField(verbose_name='Fee', max_length=100, null=True, blank=True)
    ali_usd_refund = models.FloatField(verbose_name='Refund', max_length=100, null=True, blank=True)
    ali_usd_settlement = models.FloatField(verbose_name='Settlement', max_length=100, null=True, blank=True)
    ali_cny_settlement = models.CharField(verbose_name='Rmb_settlement', max_length=100, null=True, blank=True)
    ali_currency = models.CharField(verbose_name='Currency', max_length=100, null=True, blank=True)
    ali_rate = models.FloatField(verbose_name='Rate', max_length=100, null=True, blank=True)
    ali_payment_time=models.DateTimeField(verbose_name='Payment_time', max_length=100, null=True, blank=True)
    ali_settlement_time =models.DateTimeField(verbose_name='Settlement_time', max_length=100, null=True, blank=True)
    ali_type = models.CharField(verbose_name='Type', max_length=100, null=True, blank=True)
    tm_order_status = models.CharField(verbose_name='订单状态', max_length=100, null=True, blank=True)
    tm_close_reason = models.CharField(verbose_name='订单关闭原因', max_length=100, null=True, blank=True)
    tm_order_confirm_time = models.DateTimeField(verbose_name='确认收货时间', max_length=100, null=True, blank=True)
    order_platform = models.CharField(verbose_name='订单源', max_length=100, null=True, blank=True)
    order_channel = models.CharField(verbose_name='订单出处', max_length=100, null=True, blank=True)
    order_mark = models.CharField(verbose_name='mark', max_length=100, null=True, blank=True)
    sku_usd_price = models.FloatField(verbose_name='单SKU价格USD', max_length=100, null=True, blank=True)
    sku_proportion = models.FloatField(verbose_name='占比', max_length=100, null=True, blank=True)
    sku_usd_fee = models.FloatField(verbose_name='单个SKU的Fee', max_length=100, null=True, blank=True)
    sku_usd_refund = models.FloatField(verbose_name='SKU退款金额', max_length=100, null=True, blank=True)
    sku_usd_settlement = models.FloatField(verbose_name='支付宝最终入账', max_length=100, null=True, blank=True)
    order_cost_price = models.CharField(verbose_name='订单成本价', max_length=100, null=True, blank=True)
    korean_rate = models.FloatField(verbose_name='rate2', max_length=100, null=True, blank=True)
    sku_krw_settlement = models.IntegerField(verbose_name='최종 입금 금액 KRW',  null=True, blank=True)
    sku_krw_net_income = models.IntegerField(verbose_name='수익 KRW',  null=True, blank=True)

    class Meta:
        managed = True
        app_label = 'oms'
        db_table = 'tmalloms'

    def __str__(self):
        return '%s' %(self.name)