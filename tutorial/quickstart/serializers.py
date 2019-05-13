from django.contrib.auth.models import User, Group
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username','password','is_active','email', 'groups','date_joined','last_login')
        # fields = '__all__'
        extra_kwargs = {'is_active': {'read_only': True},'is_email_verified':{'read_only': True},'First_name':{'first_name'}}

class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')