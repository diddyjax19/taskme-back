from rest_framework import serializers
from .models import CustomUser

class CreateUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        extra_kwargs = {'password': {'write_only': True}}
        fields = ['email','password']

    def create(self, validated_data):
        password = validated_data.pop('password')
        instance = self.Meta.model(**validated_data) 
        if password:
            instance.set_password(password)
        instance.save()
        return instance

class CustomSigninSerializer(serializers.Serializer):
    email = serializers.EmailField(max_length = 250, required=True)
    password = serializers.CharField(max_length = 250, required=True)
    
class SearchAPISerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id','email']