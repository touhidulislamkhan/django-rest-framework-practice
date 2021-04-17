from .models import Status  # Model
from .serializers import StatusSerializer  # Serializer based on Status model

from rest_framework.views import APIView
from rest_framework.response import Response

from rest_framework import generics, mixins

# Parsers, Viewsets
from rest_framework import parsers, viewsets

# Create your views here.


# class StatusAPIView(APIView):

#     def get(self, request, format=None):
#         status_list = Status.objects.all()
#         status_serializer = StatusSerializer(status_list, many=True)

#         return Response(status_serializer.data)


# class StatusListCreateView(generics.ListCreateAPIView):
#     queryset = Status.objects.all()
#     serializer_class = StatusSerializer
#     parser_classes = [parsers.FormParser, parsers.MultiPartParser]

# def post(self, request, *args, **kwargs):
#     return self.create(request, *args, **kwargs)


# class StatusListAPIView(generics.ListAPIView):
#     queryset = Status.objects.all()
#     serializer_class = StatusSerializer


# class StatusCreateAPIView(generics.CreateAPIView):
#     queryset = Status.objects.all()
#     serializer_class = StatusSerializer


# class StatusDetailUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Status.objects.all()
#     serializer_class = StatusSerializer
#     lookup_field = "id"
#     parser_classes = [parsers.FormParser, parsers.MultiPartParser]

# class StatusDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Status.objects.all()
#     serializer_class = StatusSerializer
#     lookup_field = "id"

# def get_object(self, *args, **kwargs):
#     kwargs = self.kwargs
#     kw_id = kwargs.get('id')

#     return Status.objects.get(id=kw_id)

# def put(self, request, *args, **kwargs):
#     return self.update(request, *args, **kwargs)

# def patch(self, request, *args, **kwargs):
#     return self.partial_update(request, *args, **kwargs)

# def delete(self, request, *args, **kwargs):
#     return self.destroy(request, *args, **kwargs)


# class StatusUpdateAPIView(generics.UpdateAPIView):
#     queryset = Status.objects.all()
#     serializer_class = StatusSerializer
#     lookup_field = "id"


# class StatusDeleteAPIView(generics.DestroyAPIView):
#     queryset = Status.objects.all()
#     serializer_class = StatusSerializer
#     lookup_field = "id"


class StatusViewset(viewsets.ModelViewSet):
    queryset = Status.objects.all()
    serializer_class = StatusSerializer
    parser_classes = [parsers.FormParser, parsers.MultiPartParser]
