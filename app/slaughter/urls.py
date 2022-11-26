from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

app_name = "slaughter"

urlpatterns = [
    path("addslaughter<anid>/", views.AddSlaughter.as_view(), name="addslaughter"),
    path("slaughterboard/", views.SlaughterBoard.as_view(), name="slaughterboard"),
    path("animaltokill/", views.AnimalToKill.as_view(), name="animaltokill"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)