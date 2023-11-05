from django.urls import path
from .views import *
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('check_booking/' , check_booking),
    path('', base, name='base'),
    path('home/', home , name='home'),
    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),
    path('hotel-detail/<uid>/' , hotel_detail , name="hotel_detail"),
    path('login/', login_page , name='login_page'),
    path('logout/', logout_page, name='logout'),
    path('register/', register_page , name='register_page'),


    path('password-reset/', auth_views.PasswordResetView.as_view(template_name='password_reset_form.html'), name='password_reset'),
    path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='password_reset_done.html'), name='password_reset_done'),
    path('password-reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html'), name='password_reset_confirm'),
    path('password-reset/complete/', auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'), name='password_reset_complete'),

]

if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)


urlpatterns += staticfiles_urlpatterns()