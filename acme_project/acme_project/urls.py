from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path



urlpatterns = [
    path('', include('pages.urls', namespace='pages')),
    path('admin/', admin.site.urls),
    path('birthday/', include('birthday.urls', namespace='birthday')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
