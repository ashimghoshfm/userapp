from django.urls import path
from . import views
from django.conf import settings
from django.contrib.staticfiles.urls import static, staticfiles_urlpatterns

urlpatterns = [
    path('', views.home, name='home'),
    path('reg/', views.reg, name='reg'),
    path('login/', views.login_page, name='login_page'),
    path('userlogin/', views.userlogin, name='userlogin'),
    path('logout/', views.userlogout, name='userlogout'),
]
urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)