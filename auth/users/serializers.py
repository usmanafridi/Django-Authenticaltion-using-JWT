from dataclasses import field, fields
from pyexpat import model
from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
   
    class Meta:
        model= User

        #These are the fields which we will use from database
        fields= ['id', 'name', 'email', 'password'] 
        extra_kwargs = {'password': {'write_only': True, 'min_length': 4}}


    def create(self, validated_data):

        """Create and return a new user."""

        password= validated_data.pop('password', None)
        instance= self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()

        return instance