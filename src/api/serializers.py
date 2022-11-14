from rest_framework import serializers
from . import models


class LogEntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.LogEntry
        fields = '__all__'
