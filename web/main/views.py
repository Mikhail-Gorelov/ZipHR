from django.shortcuts import render
from . import serializers
from rest_framework.generics import GenericAPIView


class ZipAirlinesView(GenericAPIView):
    serializer_class = serializers.ZipAirlinesSerializer

    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)
