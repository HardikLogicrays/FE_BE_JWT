
from django.urls import path
from . import views

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework_simplejwt.authentication import JWTAuthentication

schema_view = get_schema_view(
    openapi.Info(
        title="API documentation",
        default_version="v1",
        description="This Apis created for authorize user and get all the users and specific user informations.",
    ),
    public=True,
)

urlpatterns = [
    path('login/', views.LoginView.as_view()),
    path('register/', views.RegisterView.as_view()),
    path('logout/', views.LogoutView.as_view()),
    path('users/', views.UserListView.as_view()),
    path('users/<str:fullname>/', views.UserListView.as_view()),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]