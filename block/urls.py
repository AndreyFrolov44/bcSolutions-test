from django.urls import path

from .views import BlocksListView, BlockDetailView

urlpatterns = [
    path('', BlocksListView.as_view(), name='index'),
    path('blocks/<int:height>', BlockDetailView.as_view(), name='detail'),
]
