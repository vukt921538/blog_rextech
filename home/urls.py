from django.urls import path, include

from django.contrib.auth.views import LogoutView, LoginView
from home.views import *
from django.contrib.auth import views
from home.forms import LoginForm
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('', home, name='home'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('login/', views.LoginView.as_view(form_class=LoginForm), name='login'),
    path('register/', register, name='register'),
    path('<int:id>/profile', profile, name='profile'),
    path('<int:id>/update_profile', update_profile, name='update_profile'),
    path('<int:id>/content/', content, name='content'),
    path('about/', about, name='about'),
    path('<int:id>/reply/', reply_comment, name='reply_comment')
]


if settings.DEBUG:   
    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)