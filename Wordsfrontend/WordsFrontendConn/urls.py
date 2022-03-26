from django.urls import path
from WordsFrontendConn import views

urlpatterns = [
    path('', views.WordsView.as_view(),name='WordsFrontend'),
    path('detail/<int:pk>', views.WordsDetailView.as_view(),name='WordsDetail'),
]