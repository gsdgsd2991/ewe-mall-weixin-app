#from django.db import models
import json
from polls.models import *
#from serializer import Serializable
class MatchingModelView():
    '''def attributes(self):
        return [
            'id',
            'customerId', 
            'customerName',
            'name',
            'totalAmount', 
            'actualAmount', 
            'imageUrl', 
            'preferences', 
            'praises',
            'steps', 
            'comments', 
            'favorites',
            'likes',
            'genderCode', 
            'toneCode', 
            'occasionCode',
            'styleCode', 
            'keywords', 
            'content',
            'createdBy',
            'createdDate',
            'lastModifiedId', 
            'deletedDate',
            'markForDelete', 
            'optCounter', 
            'lastModified',
            'deleted', 
            'sysRandomPraisesNum',
            'sysRandomFavoritesNum', 
            'sysRandomCommentsNum']
            '''
    def __init__(self,recItem):
        self.id = recItem.id
        self.customerId = recItem.customer_id
        self.customerName = recItem.customer_name
        self.name = recItem.name
        self.totalAmount = recItem.total_amount
        self.actualAmount = recItem.actual_amount
        self.imageUrl = recItem.image_url
        self.preferences = recItem.preferences
        self.praises = recItem.praises
        self.steps = recItem.steps
        self.comments = recItem.comments
        self.favorites = recItem.favorites
        self.likes = recItem.likes
        self.genderCode = recItem.gender_code
        self.toneCode = recItem.tone_code
        self.occasionCode = recItem.occasion_code
        self.styleCode = recItem.style_code
        self.keywords = recItem.keywords
        self.content = recItem.content
        self.createdBy = recItem.created_by
        self.createdDate = str(recItem.created_date)
        self.lastModifiedId = recItem.last_modified_id
        self.deletedDate = str(recItem.deleted_date)
        self.markForDelete = recItem.mark_for_delete
        self.optCounter = recItem.opt_counter
        self.lastModified = str(recItem.last_modified)
        self.deleted = recItem.deleted
        self.sysRandomPraisesNum = recItem.sys_random_praises_num
        self.sysRandomFavoritesNum = recItem.sys_random_favorites_num
        self.sysRandomCommentsNum = recItem.sys_random_comments_num
        self.customerProfile = TblCustomer.objects.get(id = recItem.customer_id).image_url

class MatchingEncoder(json.JSONEncoder):
    def default(self, obj):
        if not isinstance(obj,MatchingModelView):
            return super(MatchingEncoder,self).default(obj)
        return obj.__dict__