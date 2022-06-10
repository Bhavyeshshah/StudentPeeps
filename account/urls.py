from django.urls import path, include
from django_email_verification import urls as email_urls
from . import views
from django.views.decorators.csrf import csrf_exempt
from .views import VerificationView
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('register', views.register, name='register'),
    path('yourdetail', views.yourdetail, name='yourdetail'),
    path('signup', views.signup, name='signup'),
    path('upload', views.upload, name='upload'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    # path('YourDetail', views.YourDetail, name='YourDetail'),
    path('email/', include(email_urls)),
    # path('send_email', views.sendEmail, name="send_email"),
    path('activate/<uidb64>/<token>', VerificationView.as_view(), name="activate"),
    path('edit_profile', views.edit_profile, name="Edit_Profile")

] 