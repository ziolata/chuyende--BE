from rest_framework import serializers
from django.contrib.auth import get_user_model, authenticate
from .models import *
# UserModel = get_user_model()
class UserSignupSerializers(serializers.ModelSerializer):
    # role_id = serializers.CharField()
    # role_name = serializers.ReadOnlyField(source='role_id.role_name')
    class Meta:
        model = UserCustom
        fields = ('username','email','password','fullname','address','phone_number',)
    def create(self, clean_data):
        user_obj = UserCustom.objects.create_user(email=clean_data['email'], password=clean_data['password'])
        user_obj.username = clean_data['username']
        # user_obj.fullname = clean_data['fullname']
        # user_obj.address = clean_data['address']
        # user_obj.phone_number = clean_data['phone_number']
        # user_obj.role_id = clean_data['role_id']
        user_obj.save()
        return user_obj 
    
class UserLoginSerializers(serializers.Serializer):
    email = serializers.EmailField
    password = serializers.CharField
    def check_user(self, clean_data):
        user = authenticate(username=clean_data['email'],password=clean_data['password'])
        if not user:
            raise ValueError('user khong ton tai')
        return user
class UserProfileSerializers(serializers.ModelSerializer):
    role_name = serializers.ReadOnlyField(source='role_id.name')
    class Meta:
        model = UserCustom
        fields = ('id','role_id','role_name','username','fullname','is_staff','is_active','address','phone_number','email','gender','birth')
class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = ('id','name')
