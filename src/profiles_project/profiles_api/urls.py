from django.conf.urls import url, include

from rest_framework.routers import DefaultRouter

from profiles_api import views

router = DefaultRouter()
router.register('hello-viewset', views.HelloViewSet, base_name='hello-viewset')
router.register('profile', views.UserProfileViewSet)
router.register('feed', views.UserProfileFeedViewSet)

urlpatterns = [
    url(r'^hello-view/', views.HelloApiView.as_view()),
    url('login/', views.UserLoginApiView.as_view()),
    url(r'', include(router.urls)),
]
