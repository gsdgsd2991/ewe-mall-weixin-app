#ewe-mall-weixin-app
This project is the server of the ewe cloth mall. Developed with python and mysql. Django is used to immplement restful api

## 微信小程序服务端
* 使用django实现的restful webapi，用于微信小程序调用。
* 后台数据库使用mysql，主要使用原有数据库表结构，新增两个managed表。
## 新增猜你喜欢api(/mysite/recommend.py)
* 利用规则，总结用户特征和搭配特征，特征矩阵相乘获得用户可能喜欢的搭配。
* api每调用一次，计算一次用户的推荐结果，前端程序可以发送请求获取用户的推荐列表
