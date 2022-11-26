from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

app_name = "cultivation"

urlpatterns = [
    path("cultivationinfoboard", views.CultivationInfoBoard.as_view(), name="cultivationinfoboard"),
    path("fodderboard", views.FodderBoard.as_view(), name="fodderboard"),
    path("addfodder", views.AddFodder.as_view(), name="addfodder"),
    path("addfodderinfo", views.AddFodderInfo.as_view(), name="addfodderinfo"),
    path("vaccineboard", views.VaccineBoard.as_view(), name="vaccineboard"),
    path("addvaccine", views.AddVaccine.as_view(), name="addvaccine"),
    path("addvaccineinfo", views.AddVaccineInfo.as_view(), name="addvaccineinfo"),
    path("turn", views.Turn.as_view(), name="turn"),
    path("addturn", views.AddTurn.as_view(), name="addturn"),
    path("quarantine", views.Quarantine.as_view(), name="quarantine"),
    path("addquarantine", views.AddQuarantine.as_view(), name="addquarantine"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)