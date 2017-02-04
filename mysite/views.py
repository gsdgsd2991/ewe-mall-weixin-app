from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import responses
from mysite.serializer import *
from polls.models import TblCustomer
from rest_framework.response import Response
from datetime import *
import time
# Create your views here.
#"name": "大 鱼 ❤️",
# "weixin_open_id": "o97I8xCwM2_8mxK6nrKCvKX-UjF8",
#"gender": "female",
#"age": null

@api_view(['GET','PUT','DELETE'])
def get_customer(request,weixinOpenId,nickname,sex):
    #customer exist
    try:
        customer = TblCustomer.objects.get(weixin_open_id=weixinOpenId)
    #customer do not exist,create customer
    except TblCustomer.DoesNotExist:
        #insert new customer
        #try:
            if sex == 1:
                gen = 'male'
            else:
                gen = 'female'
            newCus = TblCustomer(weixin_open_id=weixinOpenId, name=nickname, gender=gen,created_by=1,created_date=datetime.now(),last_modified_id=1)
            newCus.save()
            customer = TblCustomer.objects.get(weixin_open_id=weixinOpenId)
       # except:
       #     return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = CustomerSerializer(customer)
        return Response(serializer.data)
@api_view(['GET'])
def get_bodys(request,customerId):
    try:
        bodys = TblCustomerShape.objects.get(customer_id = customerId)
        serilizer = ShapeSerializer(bodys,many=True)
        return Response(serilizer.data)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['GET','PUT','DELETE'])
def create_body(request,customerId):
    try:
        body = TblCustomerShape()
        body.save()
    except:
        return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)
@api_view(['GET','PUT','DELETE'])
def create_body_image(request,img_url):
    return

@api_view(['GET','POST'])
def get_customer_list(request):
    if request.method == 'GET':
        customers = TblCustomer.objects.all()
        serializer = CustomerSerializer(customers,many=True)
        return Response(serializer.data)


