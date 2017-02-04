from polls.models import TblCustomer,TblCustomerShape
from rest_framework import serializers

class CustomerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = TblCustomer
        fields = ('name','weixin_open_id','gender','age')

class ShapeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = TblCustomerShape
        fields =  ('customization_person_name','height','weight','body_shape','face_shape','face_color','image_url','deleted')