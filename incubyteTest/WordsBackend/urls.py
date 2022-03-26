from django.urls import path
from WordsBackend import views

urlpatterns = [
    path('words/', views.WordsListView.as_view(),name='WordsList'),
    path('words/<int:pk>', views.WordsDetailView.as_view(),name='WordsDetail'),
]