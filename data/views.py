import datetime
from data.serializers import BaseAgreementSerializer, EndOfTermSerializer
from rest_framework.viewsets import ModelViewSet
from .models import BaseAgreement


class BaseAgreementViewSet(ModelViewSet):
    serializer_class = BaseAgreementSerializer
    queryset = BaseAgreement.objects.all()


class EndOfTermViewSet(ModelViewSet):
    serializer_class = EndOfTermSerializer
    queryset = BaseAgreement.objects.filter(created_at__lte=datetime.datetime.now())

