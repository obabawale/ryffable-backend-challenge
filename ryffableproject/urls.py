from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from noun import views

router = routers.DefaultRouter()
router.register(r'nouns', views.NounViewSet)
router.register(r'places', views.PlaceViewSet)
router.register(r'animals', views.AnimalViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('noun/', include('noun.urls')),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
