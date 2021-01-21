from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import SimpleRouter

from cabinets.views import auth, CabinetViewSet

router = SimpleRouter()
router.register(r'cabinets', CabinetViewSet)
# router.register(r'film_relation', UserFilmRelationView)


urlpatterns = [
    path('admin/', admin.site.urls),
    url('', include('social_django.urls', namespace='social')),
    path('auth/', auth),
    path('api/', include('cabinets.urls', namespace='api')),
]

urlpatterns += router.urls