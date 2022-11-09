from django.urls import include, path

urlpatterns = [
    path('thoth/', include('api.urls')),
]
