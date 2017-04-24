#ewe-mall-weixin-app
This project is the server of the ewe cloth mall. Developed with python and mysql. Django is used to immplement restful api

## 运行方式
* 首先安装django, pip install django.
* 安装django rest framework, pip install djangorestframework.
* 设置settings.py中的Datebase信息
* 执行数据库更改,部署程序,python manage.py migrate
* 运行程序,python manage.py runserver

## 微信小程序服务端
* 使用django实现的restful webapi，用于微信小程序调用。
* 后台数据库使用mysql，主要使用原有数据库表结构，新增两个managed表。

## 新增猜你喜欢api(/mysite/recommend.py)
* 利用规则，总结用户特征和搭配特征，特征矩阵相乘获得用户可能喜欢的搭配。
* api每调用一次，计算一次用户的推荐结果,推荐结果存储在redis中，前端程序可以发送请求获取用户的推荐列表。
* 猜你喜欢共有四个参数,其中三个分别是orderWeight,favoriteWeight,tagWeight,通过在数据库中存储这三个参数改变权重,recommend_num参数则是设置返回的推荐列表长度。
* 获取单一用户推荐列表的格式为http://127.0.0.1:8000/api-auth/get_recommend/?customer_id={customer_id},返回值为一个json格式recommend_num长度的match_id列表。
* 计算所有用户推荐列表的格式为http://127.0.0.1:8000/api-auth/start_recommend/,成功后返回200。
* 添加LFM算法实现的通过用户浏览信息进行推荐
