from django.urls import path
from .views import GaitDataList, GaitDataDetail, UserList, UserDetail

urlpatterns = [
    path('data/<int:pk>/', GaitDataDetail.as_view(), name = 'data'),
    path('',GaitDataList.as_view(), name='gait'),
    path('users/',UserList.as_view(), name='users'),
]
