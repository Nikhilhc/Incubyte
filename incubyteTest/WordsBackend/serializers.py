from .models import Words
from rest_framework import serializers

class WordSerializer(serializers.ModelSerializer):
    class Meta:
        model = Words
        fields = ['id','words']

    def get_queryset(self):
        return Words.objects.all()