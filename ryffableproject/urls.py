from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from noun import views

router = routers.DefaultRouter()
router.register(r'nouns', views.NounViewSet)
router.register(r'places', views.PlaceViewSet)
router.register(r'animals', views.AnimalViewSet)
router.register(r'foods', views.FoodViewSet)
router.register(r'things', views.ThingViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]
