from django.urls import path
from inventory.views import (
    ItemListCreateAPIView, HospitalListCreateAPIView,
    ItemRetrieveUpdateDestroyAPIView, HospitalRetrieveUpdateDestroyAPIView
)

urlpatterns = [
    path('items', ItemListCreateAPIView.as_view(), name='item-list'),
    path('items/<int:pk>', ItemRetrieveUpdateDestroyAPIView.as_view(), name='one-item'),
    path('hospital', HospitalListCreateAPIView.as_view(), name='hospital-list'),
    path('hospital/<int:pk>', HospitalRetrieveUpdateDestroyAPIView.as_view(),
         name='hospital-detail'),

]
