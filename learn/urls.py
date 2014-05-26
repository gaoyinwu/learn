from django.conf.urls import patterns, include, url
from rest_framework.urlpatterns import format_suffix_patterns

from django.contrib.auth.models import User, Group
from rest_framework import viewsets, routers

from django.contrib import admin
from learn import settings
from learn import views as learnViews
from learn import models as learnModels
admin.autodiscover()

# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    model = User

class GroupViewSet(viewsets.ModelViewSet):
    model = Group
class HistoryViewSet(viewsets.ModelViewSet):
    model = learnModels.History
class RemindViewSet(viewsets.ModelViewSet):
    model = learnModels.Remind
# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'groups', GroupViewSet)
#router.register(r"history", HistoryViewSet)
#router.register(r"remind",RemindViewSet)

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'learn.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    #url(r'^', learnViews.api_root),
    #url(r'^', include(router.urls)),
    #url(r'^', include(router.urls)),
    
    url(r'^learn/', learnViews.login),
    url(r'^logout/', learnViews.logout),
    url(r'^historys/$', learnViews.HistoryList.as_view(),name='history-list'),
    url(r'^historys/(?P<pk>[0-9]+)/$', learnViews.HistoryDetail.as_view(),name='history-detail'),

    url(r'^reminds/$', learnViews.RemindsList.as_view()),
    url(r'^reminds/history/(?P<his>[0-9]+)/$', learnViews.RemindsListByHis.as_view()),
    url(r'^reminds/(?P<his>[0-9]+)/(?P<pk>[0-9]+)/$', learnViews.RemindsDetail.as_view()),
    url(r'^remind/(?P<pk>[0-9]+)/$', learnViews.RemindDetail.as_view()),

    
    url(r'^js/(?P<path>.*)$', 'django.views.static.serve', { 'document_root': settings.BASE_DIR + '/resources/js/' }),
    url(r'^images/(?P<path>.*)$', 'django.views.static.serve', { 'document_root': settings.BASE_DIR +  '/resources/images/' }),
    url(r'^css/(?P<path>.*)$', 'django.views.static.serve', { 'document_root': settings.BASE_DIR + '/resources/css/' }),

    
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^api-docs/', include('rest_framework_swagger.urls')),
)

#urlpatterns = format_suffix_patterns(urlpatterns)