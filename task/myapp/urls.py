from .views import *
from django.urls import path


urlpatterns = [
    path('',Registrationview.as_view()),
    path('login/',loginview.as_view()),
    path('api/refresh-access-token/', RefreshAccessToken.as_view(), name='refresh-access-token'),

]
