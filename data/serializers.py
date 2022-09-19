import datetime

from rest_framework import serializers
from .models import BaseAgreement


class BaseAgreementSerializer(serializers.ModelSerializer):
    class Meta:
        model = BaseAgreement
    
    def to_representation(self, instance):
        if self.type == 'B':
            instance.amount = sum([ins.amount for ins in BaseAgreement.objects.filter(type='B')])
        return {
            "type": f"{instance.type} type Agreement",
            "total_amount": instance.amount,
            "tax": instance.amount * (0.2 - instance.exemption_rate) if instance.exemption_rate \
                else instance.amount * 0.2
        } 

class EndOfTermSerializer(serializers.ModelSerializer):
    class Meta:
        model = BaseAgreement

    def to_representation(self, instance):
        if self.type == 'B':
            instance.amount = sum([ins.amount for ins in BaseAgreement.objects.filter(type='B')])
        total_tax = sum([ins.amount * (0.2 - ins.exemption_rate) if ins.exemption_rate \
                else ins.amount * 0.2 for ins in BaseAgreement.objects.filter(created_at__lte=datetime.datetime.now())]) 
        return {
            "report_date": datetime.datetime.now().strftime("%Y-%m-%d"),
            "total_amount": sum([ins.amount for ins in BaseAgreement.objects.filter(created_at__lte=datetime.datetime.now())]),
            "total_tax": total_tax
        }