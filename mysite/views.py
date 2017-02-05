from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import responses
from mysite.serializer import *
from polls.models import *
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
#customer create or change body shape
@api_view(['POST','GET','DELETE'])
def create_body(request,customerId,name,h,w,bshape,fshape,fcolor):
    if request.method == 'POST':
        try:
            body = TblCustomerShape.objects.get(customer_id = customerId,customization_person_name=name)
            body.height = h
            body.weight = w
            body.body_shape = bshape
            body.face_shape = fshape
            body.face_color = fcolor
            body.save()
        except:
                return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    if request.method == 'GET':
        try:
            body = TblCustomerShape(customer_id = customerId,customization_person_name=name,height=h,weight=w,body_shape=bshape,face_shape=fshape,face_color=fcolor,deleted = 0)
            body.save()
        except:
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    if request.method == 'DELETE':
        shape = TblCustomerShape.objects.get(customer_id = customerId)
        shape.deleted = True
        return Response(status=status.HTTP_200_OK)

#customer upload image
@api_view(['GET','PUT','DELETE'])
def create_body_image(request,img_url):
    return Response(status = status.HTTP_200_OK)

@api_view(['GET'])
def get_matches(request,customerId):
    try:
        historys = TblCustomerMatchHistory.objects.filter(customer_id = customerId)
        serializer = HistorySerializer(historys,many=True)
        return Response(serializer.data)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['GET'])
def get_match_pic(request,matchId):
    try:
        match = EmallMatching.objects.get(id = matchId)
        serializer = MatchSerializer(match)
        return Response(serializer.data)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['GET','POST'])
def get_customers(request):
    if request.method == 'GET':
        customers = TblCustomer.objects.all()
        serializer = CustomerSerializer(customers,many=True)
        return Response(serializer.data)


