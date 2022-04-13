from rest_framework import serializers


class ZipAirlinesSerializer(serializers.Serializer):
    airplane_id = serializers.IntegerField(source='pk')
    passengers_count = serializers.IntegerField()
