from rest_framework import serializers


class ZipAirlinesSerializer(serializers.Serializer):
    first_airplane = serializers.IntegerField()
    second_airplane = serializers.IntegerField()
    third_airplane = serializers.IntegerField()
    forth_airplane = serializers.IntegerField()
    fifth_airplane = serializers.IntegerField()
    sixth_airplane = serializers.IntegerField()
    seventh_airplane = serializers.IntegerField()
    eighth_airplane = serializers.IntegerField()
    ninth_airplane = serializers.IntegerField()
    tenth_airplane = serializers.IntegerField()
    passengers_count = serializers.IntegerField()
