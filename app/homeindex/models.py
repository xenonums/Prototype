from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from imagekit.models import ProcessedImageField
from ..greatadmin.models import Animal
from ..shop.models import ListInfo


# Create your models here.
class HCategory(models.Model):
    name = models.CharField("文章类别", max_length=40, null=False)  # 分类名

    create_time = models.DateTimeField("创建时间", auto_now_add=True)
    update_time = models.DateTimeField("更新时间", auto_now_add=True)
    is_delete = models.BooleanField("删除标识", default=False)

    def __str__(self):
        return self.name
    class Meta:
        db_table = 'home_category'
        verbose_name_plural = "文章类型"
        verbose_name = "文章类型"


class HNews(models.Model):
    category = models.ForeignKey(HCategory, on_delete=models.CASCADE, verbose_name="文章内容")  # 连接分类表的外键，多对一关系
    title = models.CharField("文章标题", max_length=100, null=False)  # 标题
    author_name = models.CharField("作者名字", max_length=100, null=False)  # 作者名字
    gcontent = RichTextUploadingField("文章内容", null=False) # 富文本
    image = models.FileField("展示图", upload_to='article_image', blank=True)  # 文章配图
    views = models.IntegerField('浏览量', default=0)
    source_link = models.CharField("原文连接", max_length=200, blank=True)  # 原文链接

    create_time = models.DateTimeField("创建时间", auto_now_add=True)
    update_time = models.DateTimeField("更新时间", auto_now_add=True)
    is_delete = models.BooleanField("删除标识", default=False)

    def __str__(self):
        return self.title
    class Meta:
        db_table = 'home_news'
        verbose_name_plural = "文章"
        verbose_name = "文章"

class TBCode(models.Model):
    animal = models.ForeignKey(Animal, on_delete=models.CASCADE, verbose_name="动物id")  # 连接分类表的外键，多对一关系
    listinfo = models.ForeignKey(ListInfo, on_delete=models.CASCADE, verbose_name="清单id")  # 连接分类表的外键，多对一关系
    code = models.DecimalField(primary_key=True, verbose_name="序号", max_digits =65, decimal_places=0)
    create_time = models.DateTimeField("创建时间", auto_now_add=True)
    update_time = models.DateTimeField("更新时间", auto_now_add=True)

    def __str__(self):
        return self.name
    class Meta:
        db_table = 'home_TBCode'
        verbose_name_plural = "溯源统计表表"



