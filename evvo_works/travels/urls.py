from django.urls import path, include
from rest_framework.routers import DefaultRouter
from travels import views

router = DefaultRouter()
router.register(r'travel-requests', views.TravelRequestViewSet, basename='travel-request')

urlpatterns = [
    path('', include(router.urls)),
]   