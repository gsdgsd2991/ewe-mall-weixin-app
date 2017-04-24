from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import responses
#from mysite.serializer import *
from polls.models import *
from rest_framework.response import Response
from datetime import *
import time
from django.views.decorators.csrf import csrf_protect
import json
from mysite.recommend import *
import pickle
import redis
from django.http import HttpResponse
from mysite.ModelView import *
import serializer
import threading
import time
import mysite.log_file_rec
from  util import openId_to_id
# Create your views here.
#"name": "大 鱼 ❤️",
# "weixin_open_id": "o97I8xCwM2_8mxK6nrKCvKX-UjF8",
#"gender": "female",
#"age": null
'''
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
'''

def rec_thread():
    #while(True):
        nums = redis.Redis()
        if nums.exists('folder'):
    #Recommend.set_weight([nums['w1'],nums['w2'],nums['w3']])
            Recommend.set_log_folder(nums['folder'])
        Recommend.get_recommend_list()
        #推荐线程每24小时运行一次
     #   time.sleep(86400)

@api_view(['GET'])
def start_recommend(request):
    #weight = open('recommend_weight.pkl','rb') 
    #Recommend.set_weight([int(w) for w in pickle.load(weight)])
    #weight.close()
    #启动推荐线程
    #threading._start_new_thread(rec_thread)
    rec_thread()
    #ans = rec.recommend_dict
    return Response(status = status.HTTP_200_OK)

@api_view(['GET'])
def test_database(request):
    return Response(json.dumps(TblImCodeType.objects.filter(id=1)[0].comment))

@api_view(['GET'])
def set_recommend_num(request):
    ''' w1 = request.GET.get('orderWeight')
    w2 = request.GET.get('favoriteWeight')
    w3 = request.GET.get('tagWeight')
    recommend_num = request.GET.get('num')'''
    folder = request.GET.get('folder')

    nums = redis.Redis()
    '''nums['w1'] = w1
    nums['w2'] = w2
    nums['w3'] = w3
    nums['recommend_num'] = recommend_num'''
    nums['folder'] = folder
    #recommend_num = open('recommend_num.pkl','wb')
    #pickle.dump(num,recommend_num)
    #recommend_num.close()
    #weight = open('recommend_weight.pkl','wb')
    #pickle.dump([w1,w2,w3],weight)
    #weight.close()
    return Response(status = status.HTTP_200_OK)




@api_view(['GET'])
def get_recommend_list(request):
    openId = request.GET.get('open_id')
    id = openId_to_id(openId)#TblCustomer.objects.get(weixin_open_id = openId).id
    #id = int(request.GET.get('customer_id'))
    #return Response(serializers.Serializer(len(Recommend.recommend)).data)
    ret = '['
    ans = []
    for rec in Recommend.recommend.lrange(id,0,-1):
        ans.append(EmallMatching.objects.get(id=rec))
        ans.sort(key=lambda x:x.created_date)
        #ret.append(MatchingModelView(rec_item))
        #ret.append(MatchingModelView(rec_item).as_json())
    for rec_item in ans:
        ret +=(json.dumps( MatchingModelView(rec_item),cls=MatchingEncoder)+',')#ret.append(MatchSerializer(MatchingModelView(rec_item)).data)
        
        
        
    ret = ret[:len(ret)-1]+ ']'
    return HttpResponse(ret, content_type="application/json")#Response(json.dumps(ret))
    #return Response(json.dumps(Recommend.recommend[id]))
    
