from django.urls import include, path
from rest_framework import routers

# from evvo_works.authentication import views
from authentication import views


router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'sign-up', views.SignUpView, basename='sign-up')

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('sign-in/', views.SignInView.as_view(), name='sign-in'),  # Add the sign-in endpoint
]