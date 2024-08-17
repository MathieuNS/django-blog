from django.conf.urls.static import static
from django.contrib import admin
from django.shortcuts import redirect
from django.urls import path, include
from blog import settings
from posts.views import blog

urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog/', include('posts.urls')),
    path('', blog)
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
