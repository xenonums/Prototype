from django.contrib import admin
from app.users.models import User
from app.homeindex.models import HNews, HCategory

admin.site.register(User)
admin.site.register(HNews)
admin.site.register(HCategory)


admin.site.site_title = "系统后台"
 
admin.site.site_header = "信息平台管理"
 
admin.site.index_title = "开始您的管理"