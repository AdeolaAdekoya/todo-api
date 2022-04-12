from django.urls import path
from .views import TodoLists, TodoDetails

urlpatterns = [
    path('<int:pk>/', TodoDetails.as_view()),
    path('', TodoLists.as_view()),
]


