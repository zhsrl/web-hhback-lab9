from django.contrib import admin
from django.urls import include, path


admin.site.site_header = "Head Hunter Admin Panel"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
    path('auth/', include('authentication.urls', namespace='authentication'))
]
