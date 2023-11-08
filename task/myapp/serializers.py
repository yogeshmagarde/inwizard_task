from rest_framework import serializers
from .models import User

class Registrationserializer(serializers.ModelSerializer):
    

    class Meta:
        model=User
        fields = ["Name","email","password"]
    

class loginserializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields = ["email","password"]



class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields =['email','password']