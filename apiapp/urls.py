from django.urls import path, include
from .views import PodcastListView, PodcasterDetailView, LoginRegisterView, ContactViewSet, LogoutView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'contacts', ContactViewSet)

urlpatterns = [
    # api pathes...
    path('', PodcastListView.as_view(), name='podcastlists'),
    path('<int:pk>', PodcasterDetailView.as_view(), name='podcasterlists'),
    path('login-register/', LoginRegisterView.as_view(), name='login-register'),
    path('logout/', LogoutView.as_view(), name='api_logout'),
    path('', include(router.urls)),
    # JWT pathes...
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),
]