from django.conf.urls import patterns, include, url
from django.contrib import admin
from rest_framework import routers
from restaurants.views import RestaurantViewSet
import views

router = routers.DefaultRouter()
router.register(r'restaurants', RestaurantViewSet)

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'restaurand_api.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', views.home),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^api/v1/', include(router.urls, namespace='api')),
)
