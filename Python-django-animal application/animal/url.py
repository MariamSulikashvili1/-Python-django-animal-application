from django.urls import path
from animal.views import animalListView

urlpatterns = [
    path('animals/', animalListView.as_view()),
]
