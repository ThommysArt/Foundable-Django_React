import paypalrestsdk
from rest_framework.response import Response
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.views import APIView
from rest_framework.status import HTTP_202_ACCEPTED, HTTP_400_BAD_REQUEST
from .serializers import PaypalPaymentSerializer, PaypalPayment


class PayPalPaymentAPIView(APIView):
    serializer_class = PaypalPaymentSerializer

    def post(self, request, format=None):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            
            client_id = request.data.get('client_id')  # Get client_id from request data
            client_secret = request.data.get('client_secret')  # Get client_secret from request data

            transaction_details = request.data.get('transaction_details')  # Get transaction details from request data
            items = transaction_details.get('items')  # Get the list of items from transaction details

            paypalrestsdk.configure({
                "mode": "sandbox",  # Change to "live" for production
                "client_id": client_id,
                "client_secret": client_secret
            })

            paypal_items = []
            total_price = 0
            for item in items:
                paypal_item = {
                    "name": item.get('item_name'),
                    "sku": item.get('item_sku'),
                    "price": item.get('price'),
                    "currency": item.get('currency'),
                    "quantity": item.get('quantity')
                }
                total_price += float(item.get('price')) * int(item.get('quantity'))
                paypal_items.append(paypal_item)

            payment = paypalrestsdk.Payment({
                "intent": "sale",
                "payer": {
                    "payment_method": "paypal"
                },
                "redirect_urls": {
                    "return_url": request.data.get('return_url'),
                    "cancel_url": request.data.get('cancel_url')
                },
                "transactions": [{
                    "item_list": {
                        "items": paypal_items
                    },
                    "amount": {
                        "total": str(total_price),
                        "currency": item.get('currency')
                    },
                    "description": "Payment for multiple products"
                }]
            })

            if payment.create():
                serializer.save()
                return Response({"paymentID": payment.id}, status=HTTP_202_ACCEPTED)
            else:
                return Response({"error": payment.error})
            
        else:
            return Response({"error": "api request failed"}, status=HTTP_400_BAD_REQUEST)


class ListPaypalPaymentAPIView(ListAPIView):
    queryset = PaypalPayment.objects.all()
    serializer_class = PaypalPaymentSerializer


class RetrievePaypalPaymentAPIView(RetrieveAPIView):
    queryset = PaypalPayment.objects.all()
    serializer_class = PaypalPaymentSerializer