from django.urls import path, include
from netflixapp.API import views
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

router = DefaultRouter()

router.register('video', views.VideoList, basename ='videos')
router.register('category', views.videocategorylist, basename='videocategorylist')

urlpatterns = [
    path('', include(router.urls)),
    path('gettoken/', TokenObtainPairView.as_view(), name='token_obtain_view'),
    path('refreshtoken/', TokenRefreshView.as_view(), name='token_refresh_view'),
    path('verifytoken/', TokenVerifyView.as_view(), name='token_verify_view'),
]