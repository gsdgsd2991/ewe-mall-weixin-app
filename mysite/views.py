from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import responses
from mysite.serializer import *
from polls.models import *
from rest_framework.response import Response
from datetime import *
import time
from django.views.decorators.csrf import csrf_protect
import json
from mysite.recommend import *
# Create your views here.
#"name": "大 鱼 ❤️",
# "weixin_open_id": "o97I8xCwM2_8mxK6nrKCvKX-UjF8",
#"gender": "female",
#"age": null

@api_view(['GET','PUT','DELETE'])
def get_customer(request):
    weixinOpenId = request.GET.get('weixinOpenId')
    nickname = request.GET.get('nickname')
    sex = request.GET.get('sex')
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
#get customer all body data
@api_view(['GET'])
def get_bodys(request):
    weixinOpenId = request.GET.get('weixinOpenId')
    try:
        bodys = TblCustomerShape.objects.filter(weixin_open_id = weixinOpenId)
        #if isinstance(bodys,TblCustomerShape):
            #bodys = [bodys]
        serilizer=ShapeSerializer(bodys,many=True)
        return Response(serilizer.data)
    except Exception as e:
        print(e)
        return Response(status=status.HTTP_404_NOT_FOUND)
#customer create or change body shape
@csrf_protect
@api_view(['POST','GET','DELETE'])
def create_body(request):
    #change body
    if request.method == 'POST':
        print(request.body.decode())
        post_json = json.loads(request.body.decode())
        weixinOpenId = post_json["weixinOpenId"]
        name = post_json['name']
        h = post_json['h']
        w = post_json['w']
        bshape = post_json['bshape']
        fshape = post_json['fshape']
        fcolor = post_json['fcolor']
        sex = post_json['sex']
        try:
            body = TblCustomerShape.objects.get(weixin_open_id = weixinOpenId,customization_person_name=name)
            body.height = h
            body.weight = w
            body.body_shape = bshape
            body.face_shape = fshape
            body.face_color = fcolor
            body.sex = sex
            body.save()
            return Response(status=status.HTTP_200_OK)
        except:
                return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    #create body
    if request.method == 'GET':
        weixinOpenId = request.GET.get('weixinOpenId')
        name = request.GET.get('name')
        h = request.GET.get('h')
        w = request.GET.get('w')
        bshape = request.GET.get('bshape')
        fshape = request.GET.get('fshape')
        fcolor = request.GET.get('fcolor')
        sex = request.GET.get('sex')
        try:
            body = TblCustomerShape(weixin_open_id = weixinOpenId,customization_person_name=name,height=h,weight=w,sex = sex,body_shape=bshape,face_shape=fshape,face_color=fcolor,deleted = 0)
            body.save()
            return Response(status=status.HTTP_201_CREATED)
        except Exception as e:
            print(e)
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    #delete body
    if request.method == 'DELETE':
        shape = TblCustomerShape.objects.get(weixin_open_id = weixinOpenId,customization_person_name=name)
        shape.deleted = True
        return Response(status=status.HTTP_200_OK)

#customer upload image, not completed
@api_view(['GET','PUT','DELETE'])
def create_body_image(request,img_url):
    return Response(status = status.HTTP_200_OK)
#get all customer matches
@api_view(['GET'])
def get_matches(request):
    weixinOpenId = request.GET.get('weixinOpenId')
    name = request.GET.get('name')
    try:
        if(name != 'null'):
            historys = TblCustomerMatchHistory.objects.filter(weixin_open_id = weixinOpenId,customization_person_name=name)
        else:
            historys = TblCustomerMatchHistory.objects.filter(weixin_open_id = weixinOpenId)
        serializer = HistorySerializer(historys,many=True)
        return Response(serializer.data)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)
#get match picture
@api_view(['GET'])
def get_match(request):
    matchId = request.GET.get('matchId')
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

@api_view(['GET'])
def get_recommend(request):
    weixinOpenId = request.GET.get('weixinOpenId')

@api_view(['GET'])
def start_recommend(request):
    rec = Recommend(weight=[1,2,3]) 
    rec.get_recommend_list()
    ans = rec.recommend_dict
    return Response(status = status.HTTP_200_OK)

