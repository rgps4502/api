from django.shortcuts import render
from .models import Sms
from .serializers import SmsSerializer
from rest_framework import viewsets, status
from rest_framework.decorators import action
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
# Create your views here.
class SmsViewSet(viewsets.ModelViewSet):
    queryset = Sms.objects.all()
    serializer_class = SmsSerializer

    # [GET] /api/sms/{pk}/detail/
    @action(detail=True, methods=['get'], url_path='detail')
    def detail_action(self, request, pk=None):
        sms = get_object_or_404(Sms, pk=pk)
        result = {
            'smsc': sms.smsc,
            'timestamp': sms.timestamp
        }
        return Response(result, status=status.HTTP_200_OK)

    # [GET] /api/sms/all_smsc/
    @action(detail=False, methods=['get'], url_path='all_smsc')
    def all_smsc(self, request):
        sms = Sms.objects.values_list('smsc', flat=True).distinct()
        return Response(sms, status=status.HTTP_200_OK)