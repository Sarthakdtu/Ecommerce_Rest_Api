from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from seller.models import Seller
from seller.serialzers import SellerSerializer
# Create your views here.

@api_view(['GET'])
def api_health_check(request): 
    return Response("Seller APIs are working. Good job.")

@api_view(['GET'])
def seller_list(request):
    sellers = Seller.objects.all()
    serializer = SellerSerializer(sellers, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def seller_detail(request, pk):
    response = None
    try:
        seller = Seller.objects.get(id=pk)
        serializer = SellerSerializer(seller, many=False)
        response = serializer.data
    except:
        response = {"message":"No such seller exists.",
                     "statusCode":"0"
                    }
    return Response(response)

@api_view(['POST'])
def seller_create(request):
    serializer = SellerSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['POST'])
def seller_update(request, pk):
    response = None
    try:
        seller = Seller.objects.get(id=pk)
        serializer = SellerSerializer(instance=seller, data=request.data)
        if serializer.is_valid():
            serializer.save()
            response = serializer.data
    except:
        pass  
    if response is None:
        response = {    "message":"No such seller exists.",
                        "statusCode":"0"
                    }
    return Response(response)

@api_view(['DELETE'])
def seller_delete(request, pk):
    response = {    "message":None,
                        "statusCode":"0"
                    }
    try:
        seller = Seller.objects.get(id=pk)
        seller.delete()
        response["message"] = "Successfully deleted seller"
        response["statusCode"] = "1"
    except:
        pass  
    if response is None:
        response["message"] = "No such seller exist"
    return Response(response)
