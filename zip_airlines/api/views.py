from drf_yasg.utils import swagger_auto_schema
from rest_framework import generics
from rest_framework import mixins
from rest_framework import status
from rest_framework.response import Response

from api.models import Airplane
from api.serializers import AirplaneSerializer, AirplaneSpecSerializer


class AirplanesView(generics.ListAPIView):
    """List all planes or create multiple new ones"""
    queryset = Airplane.objects.all()
    serializer_class = AirplaneSerializer

    @swagger_auto_schema(tags=['Multiple planes'])
    def get(self, *args, **kwargs):
        return super(AirplanesView, self).get(*args, **kwargs)

    @swagger_auto_schema(tags=['Multiple planes'])
    def post(self, request, *args, **kwargs):
        """Create multiple new planes"""
        serializer = self.serializer_class(data=request.data, many=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AirplaneView(mixins.UpdateModelMixin,
                   mixins.DestroyModelMixin,
                   mixins.RetrieveModelMixin,
                   generics.GenericAPIView):
    """Operations on a single airplane, get, delete, update"""
    queryset = Airplane.objects.all()
    serializer_class = AirplaneSerializer

    @swagger_auto_schema(
        tags=['Single plane']
    )
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    @swagger_auto_schema(
        tags=['Single plane'],
    )
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    @swagger_auto_schema(
        tags=['Single plane']
    )
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


class AirplaneSpec(generics.RetrieveAPIView):
    """Get fuel consumption and duration for an airplane"""
    queryset = Airplane.objects.all()
    serializer_class = AirplaneSpecSerializer

    @swagger_auto_schema(
        tags=['Specs']
    )
    def get(self, request, *args, **kwargs):
        return super(AirplaneSpec, self).get(request, *args, **kwargs)
