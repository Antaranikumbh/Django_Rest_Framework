from django.shortcuts import render
from .models import Transaction
from rest_framework.response import Response
from .serializer import TransactionSerializer
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from django.db.models import Sum
# Create your views here.


@api_view(['GET','POST'])
def get_transaction(request):
    queryset = Transaction.objects.all().order_by('-pk')
    print(queryset)
    serializer = TransactionSerializer(queryset, many=True)

    return Response({
        "data":serializer.data,
        "total":queryset.aggregate(total=Sum('amount'))['total'] or 0
    })

class TransactionAPI(APIView):
    def get(self, request):
        queryset = Transaction.objects.all().order_by('-pk')
        print(queryset)
        serializer = TransactionSerializer(queryset,many=True)
        return Response(serializer.data)

    def post(self, request):
        data = request.data
        print(data)
        serializer = TransactionSerializer(data = data)
        if not serializer.is_valid():
            return Response ({
                "message":"data not saved",
                "error":serializer.errors,
            })
        serializer.save()
        return Response({
            "message":"data is saved",
            "data":serializer.data
           
        })

    def put(self, request):
        return Response({
            "message":" this is put request"
        })
    
    def patch(self,request):
        data = request.data
        print("id",data.get('id'))
        if not data.get('id'):
            return Response({
                "message":"data not updated",
                "errors":"id is required"
            })
        transaction = Transaction.objects.get(id= data.get('id'))
        print(transaction)
        serializer = TransactionSerializer(transaction, data=data, partial=True )
        if not serializer.is_valid():
            return Response ({
                "message":"data not saved",
                "error":serializer.errors,
            })
        serializer.save()
        return Response({
            "message":"data is saved",
            "data":serializer.data
        })
    def delete(self,request):
        data = request.data
        if not data.get('id'):
            return Response({
                "message":"data not deleted",
                "error":"id required"
            })
        transaction = Transaction.objects.get(id = data.get('id')).delete()
        return Response({
            "message":"data deleted",
            "data": {}
        })
