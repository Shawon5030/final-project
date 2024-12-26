from django.urls import path
from django.views.generic import TemplateView
from .views import *
from django.conf.urls.static import static
from .form import *
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('', home, name='index'),
    path('home/', home, name='home'),
    path('form/', Cform, name='form'),
    path('formSubmit/', formsee, name='formSubmit'),
    path('accounts/login/',auth_views.LoginView.as_view(template_name='login.html', authentication_form=LoginForm) , name='login'),
    path('registration/', CustomerRegistrationView.as_view(), name='customerregistration'),
    
    path('profile/' , profile , name='profile'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'),name='logout'),
    
    path('passwordchange/', auth_views.PasswordChangeView.as_view(template_name='passwordchange.html', form_class=MyPasswordChangeForm, success_url='/passwordchangedone/'), name='passwordchange'),
    path('passwordchangedone/', auth_views.PasswordChangeView.as_view(template_name='passwordchangedone.html'), name='passwordchangedone'),
    path('password-reset/', auth_views.PasswordResetView.as_view(template_name='password_reset.html', form_class=MyPasswordResetForm), name='password-reset'),
    path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='password_reset_done.html'), name='password_reset_done'),
    path('password-reset-complete/', auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'), name='password_reset_complete'),
    path('password-reset-confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='Shop/password_reset_confirm.html', form_class=MySetPasswordForm), name='password_reset_confirm'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)