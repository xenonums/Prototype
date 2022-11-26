from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

app_name = "shop"

urlpatterns = [
    path("saleinfoboard/", views.SaleInfoBoard.as_view(), name="saleinfoboard"),
    path("addsaleinfo/", views.AddSaleInfo.as_view(), name="addsaleinfo"),
    path("addlistinfo/", views.AddListInfo.as_view(), name="addlistinfo"),
    path("listinfoboard/", views.ListInfoBorad.as_view(), name="listinfoboard"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)