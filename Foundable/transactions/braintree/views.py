import braintree
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.status import HTTP_202_ACCEPTED, HTTP_400_BAD_REQUEST
from .serializers import BraintreePaymentSerializer, BraintreePayment

import os
from dotenv import load_dotenv, find_dotenv

ENV = load_dotenv(find_dotenv())

class BraintreePaymentAPIView(APIView):
    serializer_class = BraintreePaymentSerializer

    def post(self, request, format=None):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            gateway = braintree.BraintreeGateway(
                braintree.Configuration(
                    environment=braintree.Environment.Sandbox,
                    merchant_id=os.getenv("MERCHANT_ID"),
                    public_key=os.getenv("PUBLIC_KEY"),
                    private_key=os.getenv("PRIVATE_KEY")
                )
            )

            transaction_details = request.data.get('transaction_details')  # Get transaction details from request data
            items = transaction_details.get('items')  # Get the list of items from transaction details

            line_items = []
            total_price = 0
            for item in items:
                line_items.append({
                    "name": item.get('item_name'),
                    "quantity": item.get('quantity'),
                    "unit_amount": item.get('price'),
                    "total_amount": float(item.get('price')) * int(item.get('quantity'))
                })
                total_price += float(item.get('price')) * int(item.get('quantity'))

            result = gateway.transaction.sale({
                "amount": total_price,
                "payment_method_nonce": request.data.get('payment_method_nonce'),
                "options": {
                    "submit_for_settlement": True
                },
                "line_items": line_items
            })

            if result.is_success:
                serializer.save()
                return Response({"success": True, "transaction_id": result.transaction.id, "total_price": total_price}, status=HTTP_202_ACCEPTED)
            else:
                return Response({"success": False, "errors": result.errors.deep_errors}, status=HTTP_400_BAD_REQUEST)
            
        else:
            return Response({"success": False, "errors": serializer.errors}, status=HTTP_400_BAD_REQUEST)



class ListBraintreePaymentAPIView(ListAPIView):
    queryset = BraintreePayment.objects.all()
    serializer_class = BraintreePaymentSerializer


class RetrieveBraintreePaymentAPIView(RetrieveAPIView):
    queryset = BraintreePayment.objects.all()
    serializer_class = BraintreePaymentSerializer