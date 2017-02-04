from polls.models import TblCustomer
from rest_framework import serializers

class CustomerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = TblCustomer
        fields = ('name','weixin_open_id','gender','age')