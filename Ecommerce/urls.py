from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('app1.urls')),
    path('report_builder/', include('report_builder.urls'))
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
