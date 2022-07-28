from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from django.utils.translation import gettext_lazy as _


admin.site.index_title = _('Admin Panel')
admin.site.site_header = _('Menro Admin Panel')
admin.site.site_title = _('Menro')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('menro.urls', namespace='menro')),
]

if settings.DEBUG :
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
