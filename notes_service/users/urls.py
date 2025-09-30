from django.contrib.auth.views import LoginView, LogoutView, PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView
from . import views
from django.contrib import admin
from django.urls import include, path
from django.urls import reverse_lazy

app_name = "users"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', LoginView.as_view(template_name="registration/login.html"), name="login"),
    path('logout/',
         LogoutView.as_view(template_name="registration/logout.html"), name="logout"),
    path('register/', views.register, name="register"),
    path(
        'password_reset/',
        PasswordResetView.as_view(
            template_name="registration/password_reset_form.html",
            email_template_name="registration/password_reset_email.html",
            subject_template_name="registration/password_reset_subject.txt",
            success_url=reverse_lazy('users:password_reset_done')
        ),
        name='password_reset'
    ),
    path('password_reset/done/',
         PasswordResetDoneView.as_view(template_name="registration/password_reset_done.html"), name='password_reset_done'),
    path(
        'reset/<uidb64>/<token>/',
        PasswordResetConfirmView.as_view(
            template_name="registration/password_reset_confirm.html",
            success_url=reverse_lazy('users:password_reset_complete')
        ),
        name='password_reset_confirm'
    ),
    path('reset/done/', PasswordResetCompleteView.as_view(template_name="registration/password_reset_complete.html"),
         name='password_reset_complete'),

    path('', include(('notes.urls', 'notes'), namespace='notes')),
]
