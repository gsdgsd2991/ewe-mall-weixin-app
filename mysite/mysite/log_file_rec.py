#from polls.models import *
import redis
import json
import os
import numpy as np
import sys
from util import openId_to_id

class log_file_rec:
    def __init__(self,\
                log_folder=r'/mnt/applog/mobile-api/app',\
                weight=1,\
                ratio=0.9,\
                iter_time=100,\
                e=0.0005,\
                latent_dim=150,\
                lamb=0.001):
        self.log_folder = log_folder#log文件所在文件夹
        self.log_weight = weight#log文件权重
        self.log = redis.Redis(db=1)#用户浏览记录存储
        self.ratio=ratio#降低log权重时的系数
        self.iter_time = iter_time#迭代次数
        self.e = e#学习率
        self.latent_dim = latent_dim#latent feature dimention
        self.log_user_click_count = redis.Redis(db=2)#用户点击次数
        self.lamb = lamb#L2正则
        self.redis = redis.Redis()

    def read_log_file(self):
        '''
        读取最近的log文件,将用户的浏览行为存储的到redis中
        '''
        files = os.listdir(self.log_folder)
        files.sort()
        filename = self.log_folder+'/'+files[-2]
        with open(filename) as f:
            for str in f:
                j = json.loads(str)
                if j['action'] == 'view match detail':#浏览信息,用于协同过滤
                    id = openId_to_id(j['opendId'])
                    matchId = j['matchId']
                    if (id,matchId) not in self.log.keys():
                        self.log[(id,matchId)] = float(0.0)
                    self.log[(id,matchId)] = float(self.log[(id,matchId)])+self.log_weight#用户到搭配的对应关系
                    if id not in self.log_user_click_count.keys():
                        self.log_user_click_count[id] = 0.0
                    self.log_user_click_count[id] = float(self.log_user_click_count[id])+self.log_weight#用户点击次数增加
    
    def lowerWeight(self):
        '''
        降低之前log的权重
        '''
        for i in self.log.keys():
            self.log[i] = float(self.log[i])*self.ratio
        for i in self.log_user_click_count.keys():
            self.log_user_click_count[i] = float(self.log_user_click_count[i])*self.ratio

    def log_recommend(self):
        '''
        计算用户特征和商品特征,LFM
        '''
        self.lowerWeight()
        self.read_log_file()
        self.user_features = {}
        self.match_features = {}
        for i in self.log.keys():
            if i[0] not in self.user_features:
                self.user_features[i[0]] = np.random.random(self.latent_dim)#初始化用户特征
            if i[1] not in self.match_features:
                self.match_features[i[1]] = np.random.random(self.latent_dim)#初始化matching特征
        for i in range(self.iter_time):
            err_sum = 0
            pre_err_sum = sys.maxsize
            for user in self.user_features:
                for match in self.match_features:
                    if (user,match) in self.log:
                        pred = self.user_features[user]*self.match_features[match]
                        tempUser = self.user_features[user][:]
                        error = self.log[(user,match)]/self.log_user_click_count[user]-sum(pred)
                        for k in range(self.latent_dim):
                            self.user_features[user][k] += 2*self.e*self.match_features[match][k]*error + 2*self.lamb*self.user_features[user][k]
                            self.match_features[match][k] += 2*self.e*tempUser[k]*error + 2*self.lamb*self.match_features[match][k]
                        err_sum += sum(self.match_features[match]*self.user_features[user])**2
                        
            if err_sum > pre_err_sum:
                break
            pre_err_sum = err_sum
        rec_list = {}
        for u in  self.user_features:
            for m in self.match_features:
                rec_list[(u,m)] = sum(self.user_features[u]*self.match_features[m])
        return rec_list


