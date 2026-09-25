from django.urls import path
from . import views

urlpatterns = [
    path('api/', views.create_read),
    path('api/<int:did>', views.update_delete)
]