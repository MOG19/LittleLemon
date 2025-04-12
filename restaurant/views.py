# """
# Views for the restaurant app.
# """

# from django.shortcuts import render
# from rest_framework import generics
# from .models import Menu
# from .serializers import MenuSerializer


# def index(request):
#     """
#     Render the home page of the restaurant.
#     """
#     return render(request, 'index.html', {})


# class MenuItemsView(generics.ListCreateAPIView):
#     queryset = Menu.objects.all()
#     serializer_class = MenuSerializer


# class SingleMenuItemView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Menu.objects.all()
#     serializer_class = MenuSerializer


from django.shortcuts import render
from .models import Menu
from .serializers import MenuSerializer
from rest_framework import generics, viewsets
from .models import Menu, Booking
from .serializers import MenuSerializer, BookingSerializer
from rest_framework.permissions import IsAuthenticated


def index(request):
    """
    Render the home page of the restaurant.
    """
    return render(request, 'index.html', {})


class MenuItemsView(generics.ListCreateAPIView):
    """
    API view to list all menu items or create a new menu item.
    """
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer


class SingleMenuItemView(generics.RetrieveUpdateDestroyAPIView):
    """
    API view to retrieve, update, or delete a single menu item by ID.
    """
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer


# BookingViewSet
class BookingViewSet(viewsets.ModelViewSet):
    """
    API viewset to handle CRUD operations for table bookings.
    """
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [IsAuthenticated]
