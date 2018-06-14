from django.conf.urls import include, url
from . import views
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token, verify_jwt_token

urlpatterns = [
    url(r'^login/', obtain_jwt_token),
    url(r'^token-refresh/', refresh_jwt_token),
    url(r'^token-verify/', verify_jwt_token),
    url(r'^register/$', views.AuthRegister.as_view()),
    url(r'^test-link/$', views.test_link),
    url(r'^APX/APXPublish/$', views.apx_publish),
    url(r'^APX/APXPlaylist/(?P<uid>[0-9A-Za-z_\-]+)/$', views.apx_playlist),
    url(r'^APX/APXSchedule/(?P<uid>[0-9A-Za-z_\-]+)/$', views.apx_schedule),

    # URL Created for manual login logic
    # url(r'^login/$', AuthLogin.as_view()),
]