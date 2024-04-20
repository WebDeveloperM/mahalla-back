from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
                  path('mahalla_admin/', admin.site.urls),
                  path('api/v1/', include('task.urls')),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

admin.site.site_header = "Mahalla Admin"
admin.site.site_title = "mahalla.uz"
