from django.db import models
from utils.base_models import BaseModel
from ..users.models import User
# Create your models here.

class Animal(BaseModel):
    # birth = models.DateTimeField("转入年月")
    id = models.DecimalField(primary_key=True, verbose_name="序号", max_digits =22, decimal_places=0)
    address = models.CharField("出生地点", max_length=40)
    aclass = models.CharField("品种",max_length=10)
    fa_mo = models.CharField("父类",max_length=100)
    num = models.IntegerField("圈栏号",default=10)
    dead = models.BooleanField("是否病死",default=False)
    is_sl = models.BooleanField("是否宰杀", default=False)
    is_turn = models.BooleanField("是否转出", default=False)
    clgroup = models.ForeignKey(User, blank=True,null=True,on_delete=models.CASCADE, verbose_name='养殖企业',related_name='养殖企业')
    slgroup = models.ForeignKey(User, blank=True,null=True,on_delete=models.CASCADE, verbose_name='屠宰企业',related_name='屠宰企业')
    shgroup = models.ForeignKey(User, blank=True,null=True,on_delete=models.CASCADE, verbose_name='销售企业',related_name='销售企业')
    license = models.DecimalField(verbose_name="执照号", max_digits =22, decimal_places=0)


    class Meta:
        db_table = "pro_animal"
        verbose_name_plural = "动物信息表"
