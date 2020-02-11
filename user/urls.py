
from django.urls import path, include
from .views import UserDeatils, UserListView
urlpatterns = [
    path('api/user/<int:pk>', UserDeatils.as_view()),
    path('api/user/', UserListView.as_view())
]
