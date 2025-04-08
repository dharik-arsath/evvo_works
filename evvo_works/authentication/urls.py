from django.urls import include, path
from rest_framework import routers

from authentication import views


router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'sign-up', views.SignUpView, basename='sign-up')


urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('sign-in/', views.SignInView.as_view(), name='sign-in'), 
]