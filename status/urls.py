from django.urls import path
from .views import StatusAPIView, StatusListAPIView

urlpatterns = [
    path('status/', StatusAPIView.as_view()),
    path('list/', StatusListAPIView.as_view()),
]
