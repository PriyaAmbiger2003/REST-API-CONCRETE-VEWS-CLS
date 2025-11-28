from django.urls import path
from . import views

urlpatterns = [
    path('productapi/', views.ListCreateProductView.as_view(), name='ListCreateProductView'),
    path("productapi/<int:pk>/",views.RetrieveupdatedestroyProductView.as_view(), name='RetrieveupdatedestroyProductView'),
]
