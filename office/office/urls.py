from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include

from cabinets.views import auth

urlpatterns = [
    path('admin/', admin.site.urls),
    url('', include('social_django.urls', namespace='social')),
    path('auth/', auth),
    path('api/', include('cabinets.urls', namespace='api')),
]
