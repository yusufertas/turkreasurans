from django.db import models


class BaseAgreement(models.Model):
    type = models.CharField(max_length=1)
    agreement_no = models.IntegerField()
    amount = models.FloatField()
    address = models.TextField(max_length=1024, null=True, blank=True)
    exemption_rate = models.FloatField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)