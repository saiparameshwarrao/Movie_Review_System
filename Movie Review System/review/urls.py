
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

from django.contrib.auth import views as auth_views
from django.urls import path
from . import views

urlpatterns = [
    path('movie/<str:movie_name>/', views.movie_detail, name='movie_detail'),  
    path('', views.index, name='index'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('signup/', views.signup, name='signup'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
