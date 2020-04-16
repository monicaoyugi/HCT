from django.urls import path
from inventory.views import (
    ItemListCreateAPIView, HospitalListCreateAPIView,
    ItemRetrieveUpdateDestroyAPIView, HospitalRetrieveUpdateDestroyAPIView, DonorListCreateAPIView, DonorRetrieveUpdateDestroyAPIView,
)

urlpatterns = [
    path('items', ItemListCreateAPIView.as_view(), name='item-list'),
    path('items/<int:pk>', ItemRetrieveUpdateDestroyAPIView.as_view(), name='one-item'),
    path('hospital', HospitalListCreateAPIView.as_view(), name='hospital-list'),
    path('hospital/<int:pk>', HospitalRetrieveUpdateDestroyAPIView.as_view(),
         name='hospital-detail'),
    path('donor', DonorListCreateAPIView.as_view(), name='donor-list'),
    path('donor/<int:pk>', DonorRetrieveUpdateDestroyAPIView.as_view(),
         name='donor-detail'),
]
