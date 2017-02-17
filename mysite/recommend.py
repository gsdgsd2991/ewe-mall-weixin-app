from polls.models import *

class Recommend:
    '''
    get the recommend list
    '''
    def __init__(self):
        recommend_dict = {}
        #set time to calculate the recommend list
    def __new__(cls,*args,**kw):
        if not hasattr(cls,'_instance'):
            orig = super(Recommend,cls)
            cls._instance = orig.__new__(cls,*args,**kw)
        return cls._instance
    def get_recommend_list(self):
