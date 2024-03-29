from django.contrib import admin
from django.urls import path,include,re_path
from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve

urlpatterns = [
    path('admin/', admin.site.urls),
    path("",include("home.urls")),
    path("",include('users.urls')),
    re_path(r"media/(.*)",serve, {"document_root":settings.MEDIA_ROOT})

]
