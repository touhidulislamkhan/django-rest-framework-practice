from django.urls import path
from status import views

urlpatterns = [
    path('status/', views.StatusAPIView.as_view()),
    path('status/list/', views.StatusListAPIView.as_view()),
    path('status/create/', views.StatusCreateAPIView.as_view()),
    path('status/detail/<id>/', views.StatusDetailAPIView.as_view()),
    path('status/update/<id>/', views.StatusUpdateAPIView.as_view()),
    path('status/delete/<id>/', views.StatusDeleteAPIView.as_view()),
]
