from polls.models import *
import pickle

class Recommend:
    '''
    get the recommend list
    '''
    
    recommend = {}
    weight = [1, 1, 1]

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
    def addNum(self,matching,rate,style,gender,tone,occasion):
        
        styles = matching.style_code.split(',')
        for s in styles:
            if s in style.keys():
                style[s] += rate
            else:
                style[s] = rate
        genders = matching.gender_code.split(',')
        for g in genders:
            if g in gender.keys():
                gender[g] += rate
            else:
                gender[g] = rate
        occasions = matching.occasion_code.split(',')
        for o in occasions:
            if o in occasion.keys():
                occasion[o] += rate
            else:
                occasion[o] = rate
        tones = matching.tone_code.split(',')
        
        for t in tones:
            if t in tone.keys():
                tone[t] += rate
            else:
                tone[t] = rate
    @classmethod
    def get_recommend_list(self):
        #get matching features
        try:
            recommend_num = open('recommend_num.pkl','rb')
            N = int(pickle.load(recommend_num))
        except:
            N = 10
        finally:
            N = 10
            recommend_num.close()
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
            gender = {}
            style = {}
            tone = {}
            occasion = {}
            #the orders of customer
            orders = customer.emallorder_set.all()
            for order in orders:
                matching = order.emallorderitem_set.all()[0]
                matching = matching.match_id
                self.addNum(matching, Recommend.weight[0], style, gender, tone, occasion)
            #the favorite items of customer
            favorites = customer.emallfavorite_set.all()
            for favorite in favorites:
                matching = favorite.match_id
                self.addNum(matching, Recommend.weight[1], style, gender, tone, occasion)
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
            cus_rec_list = []
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
                cus_rec_list.append((itemKey,sum))
            cus_rec_list.sort(key=lambda x:x[1], reverse=True)
            
            cus_rec_list = cus_rec_list[0:N]
            cus_rec_list = [x[0] for x in cus_rec_list]
            Recommend.recommend[customer.id] = cus_rec_list
         

