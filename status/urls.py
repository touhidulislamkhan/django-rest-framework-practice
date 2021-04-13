from django.urls import path
from status import views

urlpatterns = [
    path('status/', views.StatusAPIView.as_view()),
    path('status/list/', views.StatusListAPIView.as_view()),
    path('status/create/', views.StatusCreateAPIView.as_view()),
]
