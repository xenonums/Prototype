from django.db import models
from utils.base_models import BaseModel, BaseModelNoDelete
from app.greatadmin.models import Animal
from ..users.models import User
# Create your models here.

class Temp(BaseModelNoDelete):
    temp = models.DecimalField("温度", max_digits=2, decimal_places=1)

    class Meta:
        db_table = "pro_temp"
        verbose_name_plural = "体温表"

class Clean(BaseModelNoDelete):
    clean = models.IntegerField("清洁度")

    class Meta:
        db_table = "pro_clean"
        verbose_name_plural = "清洁度表"

class Fodder(BaseModelNoDelete):
    user = models.ForeignKey(User, blank=True,null=True,on_delete=models.CASCADE, verbose_name='操作员')
    name = models.CharField("饲料名称", max_length=40)
    factory = models.CharField("生产厂商", max_length=40)
    license = models.CharField("批号", max_length=40)

    class Meta:
        db_table = "pro_fodder"
        verbose_name_plural = "饲料表"

class FodderInfo(BaseModelNoDelete):
    fid = models.ForeignKey(Fodder,on_delete=models.CASCADE)
    # use_date = models.DateTimeField("使用日期")
    user = models.ForeignKey(User, blank=True,null=True,on_delete=models.CASCADE, verbose_name='操作员')
    use_num = models.FloatField("使用量")


    class Meta:
        db_table = "pro_fodder_info"
        verbose_name_plural = "饲料信息表"

class Vaccine(BaseModelNoDelete):
    user = models.ForeignKey(User, blank=True,null=True,on_delete=models.CASCADE, verbose_name='操作员')
    name = models.CharField("疫苗名称", max_length=40)
    factory = models.CharField("生产厂商", max_length=40)
    license = models.CharField("批号", max_length=40)
    class Meta:
        db_table = "pro_vaccine"
        verbose_name_plural = "疫苗表"

class VaccineInfo(BaseModelNoDelete):
    vid = models.ForeignKey(Vaccine,on_delete=models.CASCADE)
    # use_date = models.DateTimeField("使用日期")
    user = models.ForeignKey(User, blank=True,null=True,on_delete=models.CASCADE, verbose_name='操作员')
    use_num = models.IntegerField("注射")


    class Meta:
        db_table = "pro_vaccine_info"
        verbose_name_plural = "疫苗信息表"

class QuarantineInfo(BaseModelNoDelete):
    # qua_date = models.DateTimeField("检疫时间")
    user = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE, verbose_name='操作员')
    qua_end = models.BooleanField("检疫结果", max_length=20)
    qua_team = models.CharField("检疫部门", max_length=20)

    class Meta:
        db_table = "pro_quarantine_info"
        verbose_name_plural = "检疫信息表"

class TurnInfo(BaseModelNoDelete):
    # ti_date = models.DateTimeField("转出时间")
    user = models.ForeignKey(User, blank=True,null=True,on_delete=models.CASCADE, verbose_name='操作员')
    sla_name = models.CharField("屠宰场名称", max_length=20)
    car_name = models.CharField("物流编号", max_length=20)

    class Meta:
        db_table = "pro_turn_info"
        verbose_name_plural = "转出信息表"

class CultivationInfo(BaseModelNoDelete):
    aid = models.ForeignKey(Animal,on_delete=models.CASCADE)
    fiid = models.ForeignKey(FodderInfo,blank=True,null=True,on_delete=models.CASCADE)
    viid = models.ForeignKey(VaccineInfo,blank=True,null=True,on_delete=models.CASCADE)
    qiid = models.OneToOneField(QuarantineInfo,blank=True,null=True,on_delete=models.CASCADE)
    temp = models.ForeignKey(Temp,blank=True,null=True,on_delete=models.CASCADE)
    clean = models.ForeignKey(Clean,blank=True,null=True,on_delete=models.CASCADE)
    tiid = models.ForeignKey(TurnInfo,blank=True,null=True,on_delete=models.CASCADE)

    class Meta:
        db_table = "pro_cultivation_info"
        verbose_name_plural = "养殖信息表"

class EnvronmentInfo(BaseModelNoDelete):
    user = models.ForeignKey(User, blank=True,null=True,on_delete=models.CASCADE, verbose_name='操作员')
    temp = models.DecimalField("温度", max_digits=2, decimal_places=1)
    humi = models.CharField("湿度", max_length=20)
    bug = models.CharField("蚊虫量", max_length=20)
    excr = models.CharField("粪便量", max_length=20)

    class Meta:
        db_table = "pro_envronment_info"
        verbose_name_plural = "环境信息表"