from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from people.models import Customer
from people.serialzers import CustomerSerializer
# Create your views here.

@api_view(['GET'])
def api_health_check(request): 
    return Response("Customer APIs are working. Good job.")

@api_view(['GET'])
def customer_list(request):
    customers = Customer.objects.all()
    serializer = CustomerSerializer(customers, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def customer_detail(request, pk):
    response = None
    try:
        customer = Customer.objects.get(id=pk)
        serializer = CustomerSerializer(customer, many=False)
        response = serializer.data
    except:
        response = {"message":"No such customer exists.",
                     "statusCode":"0"
                    }
    return Response(response)

@api_view(['POST'])
def customer_create(request):
    serializer = CustomerSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['POST'])
def customer_update(request, pk):
    response = None
    try:
        customer = Customer.objects.get(id=pk)
        serializer = CustomerSerializer(instance=customer, data=request.data)
        if serializer.is_valid():
            serializer.save()
            response = serializer.data
    except:
        pass  
    if response is None:
        response = {    "message":"No such customer exists.",
                        "statusCode":"0"
                    }
    return Response(response)

@api_view(['DELETE'])
def customer_delete(request, pk):
    response = {    "message":None,
                        "statusCode":"0"
                    }
    try:
        customer = Customer.objects.get(id=pk)
        customer.delete()
        response["message"] = "Successfully deleted customer"
        response["statusCode"] = "1"
    except:
        pass  
    if response is None:
        response["message"] = "No such customer exist"
    return Response(response)
