from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

app_name = "greatadmin"

urlpatterns = [
    path("index/", views.Index.as_view(), name="index"),
    path("", views.Index.as_view(), name="index"),
    path("editpwd/", views.Editpwd.as_view(), name="editpwd"),
    path("editprofile/", views.Edieprofile.as_view(), name="editprofile"),
    path("animalinfo/", views.AnimalInfo.as_view(), name="animalinfo"),
    path("addanimal/", views.AddAnimal.as_view(), name="addanimal"),
    path("addanimaltwo/", views.AddAnimalTwo.as_view(), name="addanimaltwo"),
    path("cultivationvision/", views.CultivationVision.as_view(), name="cultivationvision"),
    path("slaughtervision/", views.SlaughterVision.as_view(), name="slaughtervision"),
    path("marketvision/", views.MarketVision.as_view(), name="marketvision"),
    path("shopvision/", views.ShopVision.as_view(), name="shopvision"),
    path("delanimal<aid>/", views.DelAnimal.as_view(), name="delanimal"),
    path("info_multi_del/", views.info_multi_del, name="info_multi_del"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)