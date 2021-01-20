from rest_framework.routers import SimpleRouter

from cabinets.views import SeatViewSet, UserReservationsViewSet, CabinetViewSet
from django.urls import path, include

app_name = 'cabinets'

router = SimpleRouter()
router.register(r'seats', SeatViewSet)
router.register(r'cabinets', CabinetViewSet)
router.register(r'reserve', UserReservationsViewSet)

urlpatterns = [
    path('', include(router.urls)),
    # path('cabinets/', CabinetViewSet.as_view(), name='cabinets')
]

# urlpatterns += router.urls
