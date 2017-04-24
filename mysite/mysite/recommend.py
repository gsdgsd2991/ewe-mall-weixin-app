from polls.models import *
import pickle
import traceback
import redis
import json
import os
import os.path
import mysite.log_file_rec as log_file_rec
from datetime import *

class Recommend:
    '''
    get the recommend list
    '''
    
    recommend = redis.Redis()
    weight = [1, 1, 1]
    folder = r'~'
    def __init__(self):
        pass 
        #self.recommend_dict = {}
        #self.weight = weight
        #set time to calculate the recommend list

    #def __new__(cls,*args,**kw):
    #    if not hasattr(cls,'_instance'):
    #        orig = super(Recommend,cls)
    #        cls._instance = orig.__new__(cls,*args,**kw)
    #    return cls._instance

    @classmethod
    def set_weight(self,w):
            Recommend.weight = w

    @classmethod
    def set_log_folder(self,folder_path):
        self.folder = folder_path
    '''
    @classmethod
    def addNumProduct(self,product,rate,style,gender,tone,occasion):
        styles = EmallProductStyle.objects.get(product_id=product.id).code.split(',')
        for s in styles:
               if s in style:
                   style[s] += rate
               else:
                   style[s] = rate
        genders = product.gender_code.split(',')
        for g in genders:
                if g in gender:
                    gender[g] += rate
                else:
                    gender[g] = rate
        occasions = EmallProductOccasion.objects.get(product_id = product.id).code.split(',')
        for o in occasions:
                if o in occasion:
                    occasion[o] += rate
                else:
                    occasion[o] = rate
                    
        tones = product.tonal_code.split(',')
        for t in tones:
                if t in tone:
                    tone[t] += rate
                else:
                    tone[t] = rate
    '''
    @classmethod
    def addNum(self,matching,rate,style,gender,tone,occasion):
        try:
            styles = matching.style_code.split(',')
            for s in styles:
                if s in style:
                    style[s] += rate
                else:
                    style[s] = rate
            genders = matching.gender_code.split(',')
            for g in genders:
                if g in gender:
                    gender[g] += rate
                else:
                    gender[g] = rate
            occasions = matching.occasion_code.split(',')
            for o in occasions:
                if o in occasion:
                    occasion[o] += rate
                else:
                    occasion[o] = rate
            tones = matching.tone_code.split(',')
            
            for t in tones:
                if t in tone:
                    tone[t] += rate
                else:
                    tone[t] = rate
        except:
            pass

                
    @classmethod
    def get_recommend_list(self):
        try:
            N = int(TblImCodeType.objects.filter(code='recommend_num')[0].comment)
        except:
            N = 10
        (cus_id,tag_rec_dict) = self.tag_rec()
        log_folder = TblImCodeType.objects.get(code='log_folder').comment
        reviewWeight = int(TblImCodeType.objects.get(code='reviewWeight').comment)
        reviewCal_ratio = float(TblImCodeType.objects.get(code='reviewCal_ratio').comment)
        reviewCal_iter_time = int(TblImCodeType.objects.get(code='reviewCal_iter_time').comment)
        reviewCal_e = float(TblImCodeType.objects.get(code='reviewCal_e').comment)
        reviewCal_latent_dim = int(TblImCodeType.objects.get(code='reviewCal_latent_dim').comment)
        reviewCal_lamb = float(TblImCodeType.objects.get(code='reviewCal_lamb').comment)
        log = log_file_rec.log_file_rec(log_folder = log_folder,weight=reviewWeight,\
                ratio=reviewCal_ratio,iter_time=reviewCal_iter_time,e=reviewCal_e,\
                latent_dim=reviewCal_latent_dim,lamb=reviewCal_lamb)
        log_rec_dict = log.log_recommend()
        for k_log in log_rec_dict:
            if k_log[0] in tag_rec_dict and k_log[1] in tag_rec_dict[k_log[0]]:
                tag_rec_dict[k_log[0]][k_log[1]] += log_rec_dict[k_log]
        for id in cus_id:
            cus_rec = [(tag,tag_rec_dict[id][tag]) for tag in tag_rec_dict[id]]
            cus_rec.sort(key=lambda x:x[1],reverse=True)
            cus_rec = [rec[0] for rec in cus_rec]
            cus_rec = cus_rec[:N]
            Recommend.recommend.delete(id)
            Recommend.recommend.lpush(id, *cus_rec)


    @classmethod
    def tag_rec(self):
            cus_rec_list = {}
            cus_id = []
            w = []
            code = TblImCodeType.objects.filter(code = 'orderWeight')
            w.append(int(code[0].comment))
            code = TblImCodeType.objects.filter(code = 'favoriteWeight')
            w.append(int(code[0].comment))
            code = TblImCodeType.objects.filter(code = 'tagWeight')
            w.append(int(code[0].comment))
            self.set_weight(w)
            #get recommend num
            try:
                N = int(TblImCodeType.objects.filter(code='recommend_num')[0].comment)
            except:
                N = 10
            #最近的搭配编号
            recentDays = int(TblImCodeType.objects.get(code='recentDays').comment)
            recent_matchings = EmallMatching.objects.filter(created_date__gte=date.today()-timedelta(days=recentDays))
            recent_matchings = [i.id for i in recent_matchings]
            # recommend_num.close()
            items_feature = {}
            matchings = EmallMatching.objects.all()       
            for matching in matchings:     
                item_feature = {}      
                for code in matching.gender_code.split(','):
                    if code in item_feature.keys():
                        item_feature[code] += 1
                    else:
                        item_feature[code] = 1
                for code in matching.tone_code.split(','):
                    if code in item_feature.keys():
                        item_feature[code] += 1
                    else:
                        item_feature[code] = 1
                for code in matching.occasion_code.split(','):
                    if code in item_feature.keys():
                        item_feature[code] += 1
                    else:
                        item_feature[code] = 1
                for code in matching.style_code.split(','):
                    if code in item_feature.keys():
                        item_feature[code] += 1
                    else:
                        item_feature[code] = 1
                items_feature[matching.id] = item_feature
            #get customer features
            customers = TblCustomer.objects.all()
            for customer in customers:
                cus_rec_list[customer.id]=[]
                cus_id.append(customer.id)
                gender = {}
                style = {}
                tone = {}
                occasion = {}
                #the orders of customer
                orders = customer.emallorder_set.all()
                for order in orders:
                    orderItem = order.emallorderitem_set.all()[0]
                    matching = orderItem.match_id
                    self.addNum(matching, Recommend.weight[0], style, gender, tone, occasion)
                #the favorite items of customer
                favorites = customer.emallfavorite_set.all()
                for favorite in favorites:
                        self.addNum(matching, Recommend.weight[1],style, gender, tone, occasion)
                #customer customized tags
                tags = customer.emallcustomertag_set.all()
                for tag in tags:
                    if tag.type_code.strip() == 'PRODUCT_GENDER':
                        if tag.code in gender.keys():
                           gender[tag.code] += Recommend.weight[2]
                        else:
                            gender[tag.code] = Recommend.weight[2]
                    if tag.type_code.strip() == 'PRODUCT_TONE':
                        if tag.code in tone.keys():
                            tone[tag.code] += Recommend.weight[2]
                        else:
                            tone[tag.code] = Recommend.weight[2]
                    if tag.type_code.strip() == 'PRODUCT_OCCASION':
                        if tag.code in occasion.keys():
                            occasion[tag.code] += Recommend.weight[2]
                        else:
                            occasion[tag.code] = Recommend.weight[2]
                    if tag.type_code.strip() == 'PRODUCT_STYLE':
                        if tag.code in style.keys():
                            style[tag.code] += Recommend.weight[2]
                        else:
                            style[tag.code] = Recommend.weight[2]
                #calculate recommender list
                for itemKey in items_feature:
                    sum = 0
                    for g in gender:
                        if g in items_feature[itemKey].keys():
                            sum += items_feature[itemKey][g]*gender[g]
                    for s in style:
                        if s in items_feature[itemKey].keys():
                            sum += items_feature[itemKey][s]*style[s]
                    for t in tone:
                        if t in items_feature[itemKey].keys():
                            sum += items_feature[itemKey][t]*tone[t]
                    for o in occasion:
                        if o in items_feature[itemKey].keys():
                            sum += items_feature[itemKey][o]*occasion[o]
                    cus_rec_list[customer.id].append((itemKey,sum))
                cus_rec_list[customer.id].sort(key=lambda x:x[1],reverse=True)
                recentDays_recommend_ratio = TblImCodeType.objects.get(code='recentDays_recommend_ratio').comment
                #新上matching和老matching混合
                num_new = int(2*N*recentDays_recommend_ratio)
                num_old = int(2*N*(1-recentDays_recommend_ratio))
                rec_list_new = [i for i in cus_rec_list[customer.id] if i[0] in recent_matchings][:num_new]
                rec_list_old = [i for i in cus_rec_list[customer.id] if i[0] not in recent_matchings][:num_old]
                cus_rec_list[customer.id] = rec_list_new+rec_list_old#cus_rec_list[customer.id][:2*N]
                tempDict = {}
                for k,v in cus_rec_list[customer.id]:
                    tempDict[k] = v
                cus_rec_list[customer.id] = tempDict
            return (cus_id,cus_rec_list)
       

