from .models import Status  # Model
from .serializers import StatusSerializer  # Serializer based on Status model

from rest_framework.views import APIView
from rest_framework.response import Response

from rest_framework.generics import ListAPIView

# Create your views here.


class StatusAPIView(APIView):

    def get(self, request, format=None):
        status_list = Status.objects.all()
        status_serializer = StatusSerializer(status_list, many=True)

        return Response(status_serializer.data)


class StatusListAPIView(ListAPIView):
    queryset = Status.objects.all()
    serializer_class = StatusSerializer
