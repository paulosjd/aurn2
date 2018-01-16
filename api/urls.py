from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from api import views


urlpatterns = [
    url(r'^sites/$', views.SiteList.as_view()),
    url(r'^sites/(?P<pk>[0-9]+)/$', views.SiteDetail.as_view()),
    url(r'^data/$', views.DataList.as_view()),
    url(r'^data/(?P<code>\w+)/$', views.AllSiteData.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
