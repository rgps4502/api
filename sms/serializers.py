from rest_framework import serializers
from rest_framework.settings import api_settings
from sms.models import Sms

class SmsSerializer(serializers.ModelSerializer):

    timestamp = serializers.DateTimeField(format=api_settings.DATETIME_FORMAT, required = False)
    #created = serializers.DateTimeField(format=api_settings.DATETIME_FORMAT, required = False)

    class Meta:
        model = Sms
        # fields = '__all__'
        fields = ('id', 'smsc', 'timestamp', 'text', 'number')