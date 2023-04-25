from rest_framework import serializers
from .models import Task
from api.users.models import CustomUser
from api.projects.models import Project

class TaskCreationUpdationSerializer(serializers.ModelSerializer):

    user_assigned = serializers.SerializerMethodField()
    class Meta:
        model = Task
        extra_kwargs = {"user_assigned": {"write_only": False}}
        fields = ['id','project','name','description','start_date','end_date','assignedTo','state','user_assigned']

    def get_user_assigned(self,instance):
        return instance.assignedTo.email
    
    def create(self, validated_data):
        user = self.context.get('user')
        # check whether the user who is creating the task is either superuser/lead
        if user.is_staff or user.is_lead:
            assignedTo = validated_data.pop("assignedTo")
            project = validated_data.pop("project")
            
        
            instance = self.Meta.model(**validated_data)
            instance.assignedTo = assignedTo
            instance.project = project
            instance.save()
            return instance

        raise serializers.ValidationError({"Task can only be created by admin creation"})

    
    def update(self,instance,validated_data):
        user = self.context.get('user')
        # check whether the user who is creating the task is either superuser/lead
        
        assignedTo = validated_data.pop("assignedTo")
        project = validated_data.pop("project")
        
        for key,value in validated_data.items():
            setattr(instance,key,value)
            
        instance.assignedTo = assignedTo
        instance.save()
        return instance



class TaskListSerializer(serializers.ModelSerializer):
    assignedTo = serializers.CharField(source="assignedTo.email")
    class Meta:
        model = Task
        fields = ['id','name','assignedTo','state','end_date']

class CreateUpdateSubTask(serializers.ModelSerializer):
    class Meta:
        model = Task
        extra_kwargs = {"user_assigned": {"write_only": False}}
        fields = ['id','project','name','description','start_date','end_date','assignedTo','state']
    
    def create(self, validated_data):
        ParentTask = self.context.get('task')
        user = self.context.get('user')
        # check whether the user who is creating the task is lead
        if user.is_lead or user.is_staff:
            assignedTo = validated_data.pop("assignedTo")
            project = validated_data.pop("project")
        
            instance = self.Meta.model(**validated_data)
            instance.assignedTo = assignedTo
            instance.project = project
            instance.save()
            ParentTask.subtasks.add(instance)
            return instance

        raise serializers.ValidationError({"error": "Task creation rights not provided"})

        
