from polls.models import *

def openId_to_id(openId):
    '''
    将openid转换为数据库中id
    '''
    try:
        return TblCustomer.objects.get(weixin_open_id=openId).id
    except:
        return None