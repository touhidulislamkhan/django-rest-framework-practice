from django.urls import path
from status import views

# Router
from rest_framework import routers

# status/ => List, Create => GET, POST
# status/<id>/ => Details, Delete, Update => GET, DELETE, PUT/PATCH


router = routers.DefaultRouter()
router.register(r"status", views.StatusViewset, basename='status')

urlpatterns = [
    # path('status/', views.StatusAPIView.as_view()),
    # path('status/', views.StatusListCreateView.as_view()),
    # path('status/<id>/', views.StatusDetailUpdateDeleteView.as_view()),
    # path('status/<id>/', views.StatusDetailAPIView.as_view()),
    # path('status/list/', views.StatusListAPIView.as_view()),
    # path('status/create/', views.StatusCreateAPIView.as_view()),
    # path('status/detail/<id>/', views.StatusDetailAPIView.as_view()),
    # path('status/update/<id>/', views.StatusUpdateAPIView.as_view()),
    # path('status/delete/<id>/', views.StatusDeleteAPIView.as_view()),
] + router.urls
