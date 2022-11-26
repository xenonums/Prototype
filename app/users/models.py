from django.db import models
from utils.base_models import BaseModel
from django.contrib.auth.models import AbstractUser
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill

class User(AbstractUser, BaseModel):
    address = models.CharField(verbose_name='地址', max_length=500, blank=True, null=True)
    tel = models.DecimalField(verbose_name='电话', max_digits =11, decimal_places=0, blank=True, null=True)
    group = models.CharField(verbose_name='公司名', max_length=500, blank=True, null=True)
    avatar = ProcessedImageField(upload_to='avatar',
                                 default='avatar/default.png',
                                 verbose_name='头像',
                                 # 图片将处理成100 x 100的尺寸
                                 processors=[ResizeToFill(100, 100)], )
    class Meta:
        db_table = 'pro_user'
        verbose_name_plural = '用户信息'
        verbose_name = '用户信息'

class Code(models.Model):
    name = models.CharField("收货人", max_length=20)
    email = models.CharField("邮箱", max_length=20)
    code = models.CharField("验证码", max_length=50)
    create_time = models.DateTimeField("创建时间", auto_now=True)

    class Meta:
        db_table = 'pro_code'
        verbose_name_plural = '注册用户激活码'