from django.urls import path
from .views import GaitListView, gaitGraphView

urlpatterns = [
    path('data/<int:pk>/', gaitGraphView,name='gait_graph'),
    path('',GaitListView.as_view(), name='gait'),
]
