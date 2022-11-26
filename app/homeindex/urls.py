from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

app_name = "homeindex"

urlpatterns = [
    path("", views.HomeIndex.as_view(), name="homeindex"),
    path("homeindex/", views.HomeIndex.as_view(), name="homeindex"),
    path("homejvbao/", views.HomeJvbao.as_view(), name="homejvbao"),
    path("homenews/", views.HomeNews.as_view(), name="homeindex"),
    path("hometraceability/", views.HomeTraceability.as_view(), name="hometraceability"),
    path("homelegal/", views.HomeLegal.as_view(), name="homelegal"),
    path("homenotice/", views.HomeNotice.as_view(), name="homenotice"),
    path("homeexposure/", views.HomeExposure.as_view(), name="homeexposure"),
    path("homegroup/", views.HomeGroup.as_view(), name="homegroup"),
    path("homeknow/", views.HomeKnow.as_view(), name="homeknow"),
    path("homeintroduction/", views.HomeIntroduction.as_view(), name="homeintroduction"),
    path("homecomm/", views.HomeComm.as_view(), name="homecomm"),
    path("opennews<nid>/", views.OpenNews.as_view(), name="opennews"),
    path("becomeqrcode<aid>+<sid>/", views.BecomeQrcode.as_view(), name="becomeqrcode"),
    path("search", views.SearchNews.as_view(), name="search"),
    path("traceabilityinfo<aid>+<sid>/", views.TraceabilityInfo.as_view(), name="traceabilityinfo"),
    path("searchtraceability/", views.SearchTraceability.as_view(), name="searchtraceability"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)