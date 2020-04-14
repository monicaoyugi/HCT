from rest_framework.generics import GenericAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from inventory.serializers import ItemSerializer, HospitalSerializers
from inventory.models import Item, Hospital


class ItemListCreateAPIView(ListCreateAPIView):
    serializer_class = ItemSerializer
    permission_classes = (IsAuthenticated, )

    def get_queryset(self):
        return Item.objects.all()

    def post(self, request):
        data = request.data

        serializer = self.serializer_class(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        item = serializer.data
        response = {
            'item': item

        }
        return Response(response)


class ItemRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = ItemSerializer
    permission_classes = (IsAuthenticated,)
    lookup_field = 'pk'

    def get_queryset(self):
        return Item.objects.all()

    def get(self, request, pk):
        item = get_object_or_404(Item, pk=pk)
        serializer = self.serializer_class(item)
        return Response(serializer.data)

    def update(self, request, pk):
        """ update an item """
        data = request.data
        print(data)
        item = get_object_or_404(Item, pk=pk)
        serializer = self.serializer_class(item, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data)

    def delete(self, request, pk):
        """ delete an item """
        item = get_object_or_404(Item, pk=pk)
        item.delete()
        return Response({"message": "item deleted successfully"})


class HospitalListCreateAPIView(ListCreateAPIView):
    serializer_class = HospitalSerializers

    def get_queryset(self):
        return Hospital.objects.all()

    def post(self, request):
        data = request.data

        serializer = self.serializer_class(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        hospital = serializer.data
        response = {
            'hospital': hospital

        }
        return Response(response)


class HospitalRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = HospitalSerializers
    permission_classes = (IsAuthenticated,)
    lookup_field = 'pk'

    def get_queryset(self):
        return Hospital.objects.all()

    def get(self, request, pk):
        hospital = get_object_or_404(Hospital, pk=pk)
        serializer = self.serializer_class(hospital)
        return Response(serializer.data)

    def update(self, request, pk):
        data = request.data
        hospital = get_object_or_404(Hospital, pk=pk)
        serializer = self.serializer_class(hospital, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data)

    def delete(self, request, pk):
        hospital = get_object_or_404(Hospital, pk=pk)
        hospital.delete()
        return Response({"message": "user succesfully deleted"})
