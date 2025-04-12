# define URL route for index() view

"""
URL configuration for the restaurant app.
"""

from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from . import views

# urlpatterns = [
#     path('', views.index, name='index'),
#     path('menu/', views.MenuItemsView.as_view(), name='menu-list'),
#     path('menu/<int:pk>', views.SingleMenuItemView.as_view(), name='menu-detail'),
#     path('api-token-auth/', obtain_auth_token),
# ]

urlpatterns = [
    path('menu-items/', views.MenuItemsView.as_view(), name='menu-list'),
    path('menu-items/<int:pk>',
         views.SingleMenuItemView.as_view(), name='menu-detail'),
    path('api-token-auth/', obtain_auth_token),
]
