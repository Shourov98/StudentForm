from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name='homepage'),
    path('delete/<int:roll>', views.delete_student, name="delete_student"),
    path('add/', views.add_student, name="add_student"),
]
