from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import USSDEventView,ussd_view
router = DefaultRouter()

# router.register()


urlpatterns = router.urls

urlpatterns += [
    path('ussd-event/',USSDEventView.as_view(), name='ussd-event'),
    path('ussd/',ussd_view),

]