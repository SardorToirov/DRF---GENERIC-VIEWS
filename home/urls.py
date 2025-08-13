from django.urls import path
from .views import StudentListAPIView,StudentCreateAPIView,StudentUpdateAPIView,StudentDestroyAPIView


urlpatterns = [
    path('list/',StudentListAPIView.as_view()),
    path('create/',StudentCreateAPIView.as_view()),
    path('update/<int:pk>/', StudentUpdateAPIView.as_view()),
    path('destroy/<int:pk>/', StudentDestroyAPIView.as_view())

]
