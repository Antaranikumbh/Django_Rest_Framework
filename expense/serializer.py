from rest_framework import serializers
from .models import Transaction

class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = [
            "id",
            "title",
            "amount" ,
            "transaction_type",

            # fields = __all__
            
        ]
        # exclude = ['amount',]