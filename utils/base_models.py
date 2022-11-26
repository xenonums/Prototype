from django.db import models

#基模板
class BaseModel(models.Model):
    create_time = models.DateTimeField("创建时间", auto_now_add=True)
    update_time = models.DateTimeField("更新时间", auto_now_add=True)
    is_delete = models.BooleanField("删除标识", default=False)

    class Meta:
        abstract = True

class BaseModelNoDelete(models.Model):
    create_time = models.DateTimeField("创建时间", auto_now_add=True)
    update_time = models.DateTimeField("更新时间", auto_now_add=True)

    class Meta:
        abstract = True