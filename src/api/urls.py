from django.urls import path

from . import views


urlpatterns = [
    path('logs', view=views.LogListView.as_view(), name='logs'),
    path('logs/create', view=views.CreateNewEntry.as_view(), name='create'),
    path('logs/detail', view=views.LogDetailView.as_view(), name='detail'),
]
