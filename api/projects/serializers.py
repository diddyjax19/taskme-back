from rest_framework import serializers
from .models import Project
from api.users.models import CustomUser

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        extra_kwargs = {'id': {'write_only': False}}
        fields = ['id','name','avatar','start_date', 'end_date', 'description']

    def create(self, validated_data):
        user = self.context.get('user')
        if user.is_staff:
            instance = self.Meta.model.objects.create(**validated_data)
            return instance
        raise serializers.ValidationError({"Only admin/staff is allowed to make changes section" })

    def update(self, instance, validated_data):
        user = self.context.get('user')
        if user.is_staff:
            for key,value in validated_data.items():
                setattr(instance,key,value)
            instance.save()
            return instance
        raise serializers.ValidationError({"Only admin/staff is allowed to make changes section" })
        
    