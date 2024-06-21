from django.urls import path

from apps.users import views

app_name = 'api_users'

urlpatterns = [
    path('registration/', views.RegistrationAPIView.as_view(), name='registration'),
    path('confirm-email/<str:uid>/<str:token>', views.ConfirmEmailCompleteView.as_view(), name='confirm_email'),
    path('login/', views.LoginAPIView.as_view(), name='login'),
    path('logout/', views.LogoutAPIView.as_view(), name='logout'),
]
