from tastypie.resources import ModelResource
from .models import Sms


class SmsResource(ModelResource):
    class Meta:
        queryset = Sms.objects.all()
        resource_name = 'sms'
        fields = [
            "smsc",
            "timestamp",
            "text",
            "number",
        ]
        #allowed_methods = ['post']




sms_resource = SmsResource()
