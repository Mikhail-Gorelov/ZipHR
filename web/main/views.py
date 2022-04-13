from rest_framework.generics import GenericAPIView
from rest_framework.request import Request
from rest_framework.response import Response

from . import serializers
from .handler import ZipAirplane


class ZipAirlinesView(GenericAPIView):
    serializer_class = serializers.ZipAirlinesSerializer

    def post(self, request: Request, *args: list, **kwargs: dict) -> Response:
        serializer = self.get_serializer(data=request.data, many=True)
        serializer.is_valid(raise_exception=True)
        return_data = ZipAirplane.from_list(serializer.validated_data)
        return Response(return_data)
