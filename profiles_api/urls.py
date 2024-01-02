from django.urls import path, include

from rest_framework.routers import DefaultRouter
from profiles_api import views

# Register API URLs (path)

# Router HelloViewSet path
router = DefaultRouter()
router.register('hello-viewset', views.HelloViewSet, base_name='hello-viewset')

# Registering HelloAPI path
urlpatterns = [
    path('hello/', views.HelloAPIView.as_view()),
    path('', include(router.urls))
]

