from django.urls import path

from authentication.views import RegistrationApiView, LoginApiView


app_name = 'authentication'
urlpatterns = [
    path('users/', RegistrationApiView.as_view()),
    path('users/admin', LoginApiView.as_view())
]
