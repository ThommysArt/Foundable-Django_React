import stripe
from rest_framework.response import Response
from rest_framework.status import HTTP_202_ACCEPTED, HTTP_400_BAD_REQUEST
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.views import APIView
from .serializers import StripePaymentSerializer, StripePayment
import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

class StripePaymentAPIView(APIView):
    serializer_class = StripePaymentSerializer

    def post(self, request, format=None):

        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            stripe.api_key = os.getenv('STRIPE_API_KEY')

            transaction_details = request.data.get('transaction_details')  # Get transaction details from request data
            items = transaction_details.get('items')  # Get the list of items from transaction details

            line_items = []
            total_price = 0
            for item in items:
                line_item = {
                    "price_data": {
                        "currency": item.get('currency'),
                        "product_data": {
                            "name": item.get('item_name')
                        },
                        "unit_amount": int(float(item.get('price')) * 100),  # needs to be in cents
                    },
                    "quantity": item.get('quantity')
                }
                total_price += float(item.get('price')) * int(item.get('quantity'))
                line_items.append(line_item)

            session = stripe.checkout.Session.create(
                payment_method_types=['card'],
                line_items=line_items,
                mode='payment',
                success_url=request.data.get('success_url'),
                cancel_url=request.data.get('cancel_url'),
            )

            serializer.save()

            return Response({"checkout_session_id": session.id, "total_price": total_price}, status=HTTP_202_ACCEPTED)
        
        else:
            return Response({"error": "The api request failed"}, status=HTTP_400_BAD_REQUEST)


class ListStripePaymentAPIView(ListAPIView):
    queryset = StripePayment.objects.all()
    serializer_class = StripePaymentSerializer


class RetrieveStripePaymentAPIView(RetrieveAPIView):
    queryset = StripePayment.objects.all()
    serializer_class = StripePaymentSerializer

    