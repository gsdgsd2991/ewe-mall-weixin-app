from polls.models import *
from rest_framework import serializers

class CustomerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = TblCustomer
        fields = ('name','weixin_open_id','gender','age')

class ShapeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = TblCustomerShape
        fields =  ('customization_person_name','height','weight','body_shape','face_shape','face_color','image_url','deleted')
class MatchSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = EmallMatching
        fields = (image_url)

class HistorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = TblCustomerMatchHistory
        fields=('customization_person_name','match_id','last_modified','deleted')