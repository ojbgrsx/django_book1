from django.urls import path
from . import views

urlpatterns = [
    path('', views.book_view),
    path('book_details/<int:id>/', views.book_details_view),
]