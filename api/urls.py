from django.urls import path
from expense import views


urlpatterns = [
    path("get-transaction/",views.get_transaction),
    path('transactions/',views.TransactionAPI.as_view())
]