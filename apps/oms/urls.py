from django.urls import path
from rest_framework.routers import DefaultRouter
from oms.views import SkuListViewSet


router = DefaultRouter()

router.register('skulists',SkuListViewSet, basename='skulists') #http://127.0.0.1/incross/skulists
urlpatterns = [ ]

urlpatterns += router.urls