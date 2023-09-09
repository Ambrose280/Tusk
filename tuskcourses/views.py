from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from django.core.mail import send_mail
# Create your views here.
from django.db.models import Q
from .serializers import *
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import *
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
import stripe
from dotenv import load_dotenv
import os
from djstripe.models import *




@api_view(['GET'])
@permission_classes([IsAuthenticated])
def endpoints(request):
    data = ['Course API']
    return Response(data)


@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def stripe_prices(request):
    if request.method == 'GET':
        query = request.GET.get('query', '')

        # Use Q objects to perform a case-insensitive search in title and description fields
        prices = Price.objects.filter(Q(id__icontains=query))
        serializer = PriceSerializer(prices, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    if request.method == 'POST':
        serializer = PriceSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    
@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def stripe_price_detail(request, pk):
    try:
        price = Price.objects.get(pk=pk)
    except Price.DoesNotExist:
        return Response({"detail": "Price not found"}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = PriceSerializer(price, many=False)
        return Response(serializer.data, status=status.HTTP_200_OK)

    if request.method == 'PUT':
        serializer = PriceSerializer(price, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'DELETE':
        price.delete()
        return Response({"detail": "Price deleted successfully"}, status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def plan(request):
    if request.method == 'GET':
        query = request.GET.get('query', '')

        # Use Q objects to perform a case-insensitive search in title and description fields
        plans = Plan.objects.filter(Q(id__icontains=query))
        serializer = PriceSerializer(plans, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    if request.method == 'POST':
        serializer = PriceSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    
@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def plan_detail(request, pk):
    try:
        plan = Plan.objects.get(pk=pk)
    except Plan.DoesNotExist:
        return Response({"detail": "Plan not found"}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = PlanSerializer(plan, many=False)
        return Response(serializer.data, status=status.HTTP_200_OK)

    if request.method == 'PUT':
        serializer = PlanSerializer(plan, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'DELETE':
        plan.delete()
        return Response({"detail": "Plan deleted successfully"}, status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def sessionlist(request):
    if request.method == 'GET':
        query = request.GET.get('query', '')

        # Use Q objects to perform a case-insensitive search in title and description fields
        sessions = Session.objects.filter(Q(id__icontains=query))
        serializer = SessionSerializer(sessions, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    if request.method == 'POST':
        serializer = SessionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    
@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def session_detail(request, pk):
    try:
        session = Session.objects.get(pk=pk)
    except Session.DoesNotExist:
        return Response({"detail": "Session not found"}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = SessionSerializer(session, many=False)
        return Response(serializer.data, status=status.HTTP_200_OK)

    if request.method == 'PUT':
        serializer = SessionSerializer(session, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'DELETE':
        plan.delete()
        return Response({"detail": "Session deleted successfully"}, status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def subscriptionitems(request):
    if request.method == 'GET':
        query = request.GET.get('query', '')

        # Use Q objects to perform a case-insensitive search in title and description fields
        subscriptionitems = Subscription.objects.filter(Q(id__icontains=query))
        serializer = SubscriptionSerializer(subscriptionitems, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    if request.method == 'POST':
        # Create a customer
        customer = stripe.Customer.create(source="tok_visa",  email="customer@example.com")
        subscription = stripe.Subscription.create(customer=customer.id, items=[{"price": "price_12345",},])

    
@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def subscriptionitem(request, pk):
    try:
        subscription = Subscription.objects.get(pk=pk)
    except Subscription.DoesNotExist:
        return Response({"detail": "Subscription not found"}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = SubscriptionSerializer(subscriptionitem, many=False)
        return Response(serializer.data, status=status.HTTP_200_OK)

    if request.method == 'PUT':
        serializer = SubscriptionSerializer(subscriptionitem, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'DELETE':
        subscription.delete()
        return Response({"detail": "Subscription deleted successfully"}, status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def paymentmethods(request):
    if request.method == 'GET':
        query = request.GET.get('query', '')

        # Use Q objects to perform a case-insensitive search in title and description fields
        paymentmethods = PaymentMethod.objects.filter(Q(id__icontains=query))
        serializer = PaymentMethodSerializer(paymentmethods, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    if request.method == 'POST':
        serializer = PaymentMethodSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    
@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def paymentmethod(request, pk):
    try:
        paymentmethod = PaymentMethod.objects.get(pk=pk)
    except PaymentMethod.DoesNotExist:
        return Response({"detail": "Payment Method not found"}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = PaymentMethodSerializer(paymentmethod, many=False)
        return Response(serializer.data, status=status.HTTP_200_OK)

    if request.method == 'PUT':
        serializer = PaymentMethodSerializer(paymentmethod, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'DELETE':
        paymentmethod.delete()
        return Response({"detail": "Payment Method deleted successfully"}, status=status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def refunditems(request):
    if request.method == 'GET':
        query = request.GET.get('query', '')

        # Use Q objects to perform a case-insensitive search in title and description fields
        refunditems = Refund.objects.filter(Q(id__icontains=query))
        serializer = RefundSerializer(refunditems, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    if request.method == 'POST':
        serializer = RefundSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    
@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def refunditem(request, pk):
    try:
        refunditem = Refund.objects.get(pk=pk)
    except Refund.DoesNotExist:
        return Response({"detail": "Refund not found"}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = RefundSerializer(refunditem, many=False)
        return Response(serializer.data, status=status.HTTP_200_OK)

    if request.method == 'PUT':
        serializer = RefundSerializer(refunditem, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'DELETE':
        refunditem.delete()
        return Response({"detail": "Refund deleted successfully"}, status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def setupintent(request):
    if request.method == 'GET':
        query = request.GET.get('query', '')

        # Use Q objects to perform a case-insensitive search in title and description fields
        setup_intent = SetupIntent.objects.filter(Q(id__icontains=query))
        serializer = SetupIntentSerializer(setup_intent, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    if request.method == 'POST':
        serializer = SetupIntentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    
@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def setupintent_detail(request, pk):
    try:
        setupintent = InvoiceItem.objects.get(pk=pk)
    except InvoiceItem.DoesNotExist:
        return Response({"detail": "Setup Intent not found"}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = SetupIntentSerializer(setupintent, many=False)
        return Response(serializer.data, status=status.HTTP_200_OK)

    if request.method == 'PUT':
        serializer = SetupIntentSerializer(setupintent, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'DELETE':
        setupintent.delete()
        return Response({"detail": "Setup Intent deleted successfully"}, status=status.HTTP_204_NO_CONTENT)




@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def invoice_items(request):
    if request.method == 'GET':
        query = request.GET.get('query', '')

        # Use Q objects to perform a case-insensitive search in title and description fields
        invoice_item = InvoiceItem.objects.filter(Q(id__icontains=query))
        serializer = InvoiceItemSerializer(invoice_item, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    if request.method == 'POST':
        serializer = InvoiceItemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    
@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def invoice_item(request, pk):
    try:
        invoice_item = InvoiceItem.objects.get(pk=pk)
    except InvoiceItem.DoesNotExist:
        return Response({"detail": "Invoice Item not found"}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = InvoiceItemSerializer(invoice_item, many=False)
        return Response(serializer.data, status=status.HTTP_200_OK)

    if request.method == 'PUT':
        serializer = InvoiceItemSerializer(invoice_item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'DELETE':
        invoice_item.delete()
        return Response({"detail": "Invoice Item deleted successfully"}, status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def payment_intents(request):
    if request.method == 'GET':
        query = request.GET.get('query', '')

        # Use Q objects to perform a case-insensitive search in title and description fields
        payment_item = PaymentIntent.objects.filter(Q(id__icontains=query))
        serializer = PaymentIntentSerializer(payment_item, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    if request.method == 'POST':
        serializer = PaymentIntentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    
@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def payment_intent(request, pk):
    try:
        paymentitem = PaymentIntent.objects.get(pk=pk)
    except PaymentIntent.DoesNotExist:
        return Response({"detail": "Payment Intent not found"}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = PaymentIntentSerializer(paymentitem, many=False)
        return Response(serializer.data, status=status.HTTP_200_OK)

    if request.method == 'PUT':
        serializer = PaymentIntentSerializer(paymentitem, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'DELETE':
        paymentitem.delete()
        return Response({"detail": "Payment Intent deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
    



@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def payout_items(request):
    if request.method == 'GET':
        query = request.GET.get('query', '')

        # Use Q objects to perform a case-insensitive search in title and description fields
        payment_item = Payout.objects.filter(Q(id__icontains=query))
        serializer = PayoutSerializer(payment_item, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    if request.method == 'POST':
        serializer = PayoutSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    
@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def payout_item(request, pk):
    try:
        paymentitem = Payout.objects.get(pk=pk)
    except Payout.DoesNotExist:
        return Response({"detail": "Payout not found"}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = PayoutSerializer(paymentitem, many=False)
        return Response(serializer.data, status=status.HTTP_200_OK)

    if request.method == 'PUT':
        serializer = PayoutSerializer(paymentitem, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'DELETE':
        paymentitem.delete()
        return Response({"detail": "Payout Log deleted successfully"}, status=status.HTTP_204_NO_CONTENT)




@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def stripe_products(request):
    if request.method == 'GET':
        query = request.GET.get('query', '')
        stripe.Product.create(name="Gold Special")

        # Use Q objects to perform a case-insensitive search in title and description fields
        prods = Product.objects.filter(Q(description__icontains=query))
        serializer = ProductSerializer(prods, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    if request.method == 'POST':
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    
@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def stripe_product_detail(request, pk):
    try:
        prods = Product.objects.get(pk=pk)
    except Product.DoesNotExist:
        return Response({"detail": "Stripe Product not found"}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ProductSerializer(prods, many=False)
        return Response(serializer.data, status=status.HTTP_200_OK)

    if request.method == 'PUT':
        serializer = ProductSerializer(prods, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'DELETE':
        prods.delete()
        return Response({"detail": "Stripe Product deleted successfully"}, status=status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def subscriptions(request):
    if request.method == 'GET':
        query = request.GET.get('query', '')

        # Use Q objects to perform a case-insensitive search in title and description fields
        subscriptionitems = Subscription.objects.filter(Q(id__icontains=query))
        serializer = SubscriptionSerializer(subscriptionitems, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    if request.method == 'POST':
        serializer = SubscriptionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    
@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def subscription(request, pk):
    try:
        subscriptionitem = Subscription.objects.get(pk=pk)
    except Subscription.DoesNotExist:
        return Response({"detail": "Subscription not found"}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = SubscriptionSerializer(subscriptionitem, many=False)
        return Response(serializer.data, status=status.HTTP_200_OK)

    if request.method == 'PUT':
        serializer = SubscriptionSerializer(subscriptionitem, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'DELETE':
        subscriptionitem.delete()
        return Response({"detail": "Subscription deleted successfully"}, status=status.HTTP_204_NO_CONTENT)



@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def languages(request):
    if request.method == 'GET':
        query = request.GET.get('query', '')

        # Use Q objects to perform a case-insensitive search in title and description fields
        users = Language.objects.filter(Q(language__icontains=query))
        serializer = LanguageSerializer(users, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    if request.method == 'POST':
        serializer = LanguageSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    
@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def language_detail(request, pk):
    try:
        langs = Language.objects.get(pk=pk)
    except Language.DoesNotExist:
        return Response({"detail": "Language not found"}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = LanguageSerializer(langs, many=False)
        return Response(serializer.data, status=status.HTTP_200_OK)

    if request.method == 'PUT':
        serializer = LanguageSerializer(langs, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'DELETE':
        langs.delete()
        return Response({"detail": "Language deleted successfully"}, status=status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def customers(request):
    if request.method == 'GET':
        query = request.GET.get('query', '')

        # Use Q objects to perform a case-insensitive search in title and description fields
        customer_list = Customer.objects.filter(Q(id__icontains=query))
        serializer = CustomerSerializer(customer_list, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    if request.method == 'POST':
        serializer = CustomerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    
@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def customer_detail(request, pk):
    try:
        customer_detail = Customer.objects.get(pk=pk)
    except Subscription.DoesNotExist:
        return Response({"detail": "Customer not found"}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = CustomerSerializer(customer_detail, many=False)
        return Response(serializer.data, status=status.HTTP_200_OK)

    if request.method == 'PUT':
        serializer = CustomerSerializer(customer_detail, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'DELETE':
        customer_detail.delete()
        return Response({"detail": "Customer deleted successfully"}, status=status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def customers(request):
    if request.method == 'GET':
        query = request.GET.get('query', '')

        # Use Q objects to perform a case-insensitive search in title and description fields
        discount = Discount.objects.filter(Q(id__icontains=query))
        serializer = DiscountSerializer(discount, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    if request.method == 'POST':
        serializer = DiscountSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    
@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def discount_detail(request, pk):
    try:
        discount_detail = Discount.objects.get(pk=pk)
    except Discount.DoesNotExist:
        return Response({"detail": "Discount not found"}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = DiscountSerializer(discount_detail, many=False)
        return Response(serializer.data, status=status.HTTP_200_OK)

    if request.method == 'PUT':
        serializer = DiscountSerializer(discount_detail, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'DELETE':
        discount_detail.delete()
        return Response({"detail": "Discount deleted successfully"}, status=status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def users(request):
    if request.method == 'GET':
        query = request.GET.get('query', '')

        # Use Q objects to perform a case-insensitive search in title and description fields
        users = User.objects.filter(Q(username__icontains=query))
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    if request.method == 'POST':
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    
@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def user_detail(request, pk):
    try:
        users = Course.objects.get(pk=pk)
    except Course.DoesNotExist:
        return Response({"detail": "User not found"}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = UserSerializer(users, many=False)
        return Response(serializer.data, status=status.HTTP_200_OK)

    if request.method == 'PUT':
        serializer = UserSerializer(users, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'DELETE':
        users.delete()
        return Response({"detail": "User deleted successfully"}, status=status.HTTP_204_NO_CONTENT)



@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def courses_list(request):
    if request.method == 'GET':
        query = request.GET.get('query', '')

        # Use Q objects to perform a case-insensitive search in title and description fields
        courses = Course.objects.filter(Q(title__icontains=query) | Q(description__icontains=query))
        serializer = CourseSerializer(courses, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    if request.method == 'POST':
        serializer = CourseSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    
@api_view(['GET', 'PUT', 'DELETE', 'PATCH'])
@permission_classes([IsAuthenticated])
def course_details(request, pk):
    try:
        cours_e = Course.objects.get(pk=pk)
    except Course.DoesNotExist:
        return Response({"detail": "Course not found"}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = CourseSerializer(cours_e, many=False)
        return Response(serializer.data, status=status.HTTP_200_OK)

    if request.method == 'PUT':
        serializer = CourseSerializer(cours_e, data=request.data) 
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    if request.method == 'DELETE':
        cours_e.delete()
        return Response({"detail": "Course deleted successfully"}, status=status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def course_categories_list(request):
    if request.method == 'GET':
        query = request.GET.get('query', '')

        # Use Q objects to perform a case-insensitive search in name field
        course_categories = CourseCategory.objects.filter(Q(name__icontains=query))
        serializer = CourseCategorySerializer(course_categories, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    if request.method == 'POST':
        serializer = CourseCategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def course_categories_details(request, pk):
    try:
        course_category = CourseCategory.objects.get(pk=pk)
    except CourseCategory.DoesNotExist:
        return Response({"detail": "Course category not found"}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = CourseCategorySerializer(course_category, many=False)
        return Response(serializer.data, status=status.HTTP_200_OK)

    if request.method == 'PUT':
        serializer = CourseCategorySerializer(course_category, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response('Course category was edited', status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'DELETE':
        course_category.delete()
        return Response('Course category was deleted', status=status.HTTP_204_NO_CONTENT)
    

@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def course_modules_list(request):
    if request.method == 'GET':
        query = request.GET.get('query', '')

        # Use Q objects to perform a case-insensitive search in title field
        course_modules = CourseModule.objects.filter(Q(title__icontains=query))
        serializer = CourseModuleSerializer(course_modules, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    if request.method == 'POST':
        serializer = CourseModuleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def course_module_details(request, pk):
    try:
        course_module = CourseModule.objects.get(pk=pk)
    except CourseModule.DoesNotExist:
        return Response({"detail": "Course module not found"}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = CourseModuleSerializer(course_module)
        return Response(serializer.data, status=status.HTTP_200_OK)

    if request.method == 'PUT':
        serializer = CourseModuleSerializer(course_module, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"detail": "Course module detail was edited"}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'DELETE':
        course_module.delete()
        return Response({"detail": "Course module detail was deleted"}, status=status.HTTP_204_NO_CONTENT)

    
@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def course_sub_modules_list(request):
    if request.method == 'GET':
        query = request.GET.get('query', '')

        # Use Q objects to perform a case-insensitive search in title field
        course_sub_modules = CourseSubModule.objects.filter(Q(title__icontains=query))
        serializer = CourseSubModuleSerializer(course_sub_modules, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    if request.method == 'POST':
        serializer = CourseSubModuleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def course_sub_module_details(request, pk):
    try:
        course_sub_module = CourseSubModule.objects.get(pk=pk)
    except CourseSubModule.DoesNotExist:
        return Response({"detail": "Course sub-module not found"}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = CourseSubModuleSerializer(course_sub_module)
        return Response(serializer.data, status=status.HTTP_200_OK)

    if request.method == 'PUT':
        serializer = CourseSubModuleSerializer(course_sub_module, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"detail": "Course sub-module detail was edited"}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'DELETE':
        course_sub_module.delete()
        return Response({"detail": "Course sub-module detail was deleted"}, status=status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def course_module_quizzes(request):
    if request.method == 'GET':
        query = request.GET.get('query', '')
        course_module_quizzes = CourseModuleQuiz.objects.filter(Q(question__icontains=query))
        serializer = CourseModuleQuizSerializer(course_module_quizzes, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    if request.method == 'POST':
        serializer = CourseModuleQuizSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def course_module_quizzes_details(request, pk):
    try:
        course_module_quiz = CourseModuleQuiz.objects.get(pk=pk)
    except CourseModuleQuiz.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = CourseModuleQuizSerializer(course_module_quiz)
        return Response(serializer.data, status=status.HTTP_200_OK)

    if request.method =='PUT':
        serializer = CourseModuleQuizSerializer(course_module_quiz, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method =='DELETE':
        course_module_quiz.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def course_sub_module_quizzes(request):
    if request.method == 'GET':
        query = request.GET.get('query', '')
        course_sub_modules = CourseSubModuleQuiz.objects.filter(Q(question__icontains=query))
        serializer = CourseSubModuleQuizSerializer(course_sub_modules, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    if request.method == 'POST':
        serializer = CourseSubModuleQuizSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def course_sub_module_quizzes_details(request, pk):
    try:
        course_sub_module_quiz = CourseSubModuleQuiz.objects.get(pk=pk)
    except CourseSubModuleQuiz.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = CourseSubModuleQuizSerializer(course_sub_module_quiz)
        return Response(serializer.data, status=status.HTTP_200_OK)

    if request.method =='PUT':
        serializer = CourseSubModuleQuizSerializer(course_sub_module_quiz, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method =='DELETE':
        course_sub_module_quiz.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def course_module_quiz_answers(request):
    if request.method == 'GET':
        query = request.GET.get('query', '')
        course_module_answers = CourseModuleQuizAnswer.objects.filter(Q(answers__icontains=query))
        serializer = CourseModuleQuizAnswerSerializer(course_module_answers, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    if request.method == 'POST':
        serializer = CourseModuleQuizAnswerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def course_module_quiz_answers_details(request, pk):
    try:
        course_module_answer = CourseModuleQuizAnswer.objects.get(pk=pk)
    except CourseModuleQuizAnswer.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = CourseModuleQuizAnswerSerializer(course_module_answer)
        return Response(serializer.data, status=status.HTTP_200_OK)

    if request.method =='PUT':
        serializer = CourseModuleQuizAnswerSerializer(course_module_answer, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method =='DELETE':
        course_module_answer.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    


@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def course_sub_module_quiz_answers(request):
    if request.method == 'GET':
        query = request.GET.get('query', '')
        course_sub_module_answers = CourseSubModuleQuizAnswer.objects.filter(Q(answers__icontains=query))
        serializer = CourseSubModuleQuizAnswerSerializer(course_sub_module_answers, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    if request.method == 'POST':
        serializer = CourseSubModuleQuizAnswerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def course_sub_module_quiz_answers_details(request, pk):
    try:
        course_sub_module_answer = CourseSubModuleQuizAnswer.objects.get(pk=pk)
    except CourseSubModuleQuizAnswer.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = CourseSubModuleQuizAnswerSerializer(course_sub_module_answer)
        return Response(serializer.data, status=status.HTTP_200_OK)

    if request.method =='PUT':
        serializer = CourseSubModuleQuizAnswerSerializer(course_sub_module_answer, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method =='DELETE':
        course_sub_module_answer.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def course_reviews(request):
    if request.method == 'GET':
        query = request.GET.get('query', '')
        course_reviews = CourseReview.objects.filter(Q(reviewmsg__icontains=query))
        serializer = CourseReviewSerializer(course_reviews, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    if request.method == 'POST':
        serializer = CourseReviewSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def course_review_details(request, pk):
    try:
        course_review = CourseReview.objects.get(pk=pk)
    except CourseReview.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = CourseReviewSerializer(course_review)
        return Response(serializer.data, status=status.HTTP_200_OK)

    if request.method =='PUT':
        serializer = CourseReviewSerializer(course_review, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method =='DELETE':
        course_review.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)




