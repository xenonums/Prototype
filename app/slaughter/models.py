from django.db import models
from ..users.models import User
from ..cultivation.models import CultivationInfo
from ..greatadmin.models import Animal
from utils.base_models import BaseModelNoDelete

class Slaughter(BaseModelNoDelete):
    aeid = models.ForeignKey(User, on_delete=models.CASCADE,verbose_name='操作员')
    # slau_date = models.DateTimeField("屠宰时间")
    patch = models.CharField("身体部位", max_length=20)

    class Meta:
        db_table = 'pro_slaughter'
        verbose_name_plural = '屠宰'

# 屠宰检疫数据、屠宰厂信息表后期还需改进
# 动物/屠宰员/屠宰场信息为属性的表

class SlaughterInfo(BaseModelNoDelete):
    user = models.ForeignKey(User, blank=True,null=True,on_delete=models.CASCADE, verbose_name='操作员')
    aid = models.ForeignKey(Animal, on_delete=models.CASCADE)
    sid = models.ForeignKey(Slaughter, on_delete=models.CASCADE)
    safe = models.BooleanField("检疫情况")
    is_in = models.BooleanField("是否入库", default=False)
    license = models.DecimalField("屠宰场编号号", max_digits=22, decimal_places=0)

    class Meta:
        db_table = 'pro_slaughter_info'
        verbose_name_plural = '屠宰信息'