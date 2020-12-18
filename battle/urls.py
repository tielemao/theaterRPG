from django.contrib import admin
from django.urls import path
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.conf import settings
from login import views
from fight.views import uploadImg, showImg


urlpatterns = [
    path('admin/', admin.site.urls),
    path('fight/', include('fight.urls')),
    path('index/', views.index, name='index'),
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('logout/', views.logout),
    path('captcha/', include('captcha.urls')),
    path('uploadImg/', uploadImg),
    path('showImg/', showImg),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
