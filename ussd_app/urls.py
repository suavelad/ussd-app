from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import USSDView,ussd_view
router = DefaultRouter()

# router.register()


urlpatterns = router.urls

urlpatterns += [
    # path('ussd/',USSDView.as_view(), name='ussd'),
    path('ussd/',ussd_view),

]