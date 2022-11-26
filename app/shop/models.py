from django.db import models
from utils.base_models import BaseModel, BaseModelNoDelete
from ..slaughter.models import SlaughterInfo
from ..users.models import User
# Create your models here.
class SaleInfo(BaseModelNoDelete):
    siid = models.OneToOneField(SlaughterInfo,on_delete=models.CASCADE)
    name = models.ForeignKey(User, blank=True,null=True,on_delete=models.CASCADE, verbose_name='操作员')
    lisence = models.CharField("销售许可证", max_length=20)   # license写错了！！！！！！
    # t_date = models.DateTimeField("转入时间")
    price = models.DecimalField("单价", max_digits=5, decimal_places=2)

    class Meta:
        db_table = "pro_sale_info"
        verbose_name_plural = "销售信息表"


class ListInfo(BaseModelNoDelete):
    user = models.ForeignKey(User, blank=True,null=True,on_delete=models.CASCADE, verbose_name='操作员')
    saiid = models.ForeignKey(SaleInfo,on_delete=models.CASCADE)
    # t_data = models.DateTimeField("销售时间")
    heavy = models.IntegerField("销售肉块重量",)  # 可否将Slaugher的patch也设置重量，之后与heavy做判断，判断是否受空？
    day = models.IntegerField("保质期", )
    price = models.DecimalField("出售价格", max_digits=5, decimal_places=2)

    class Meta:
        db_table = "pro_list_info"
        verbose_name_plural = "销售清单信息表"

class Passage(BaseModelNoDelete):
    uid = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='操作员')
    passage = models.TextField("商品简介",max_length=400)

    class Meta:
        db_table = "pro_passage"
        verbose_name_plural = "备忘录信息表"