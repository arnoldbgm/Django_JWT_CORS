from rest_framework import serializers
from django.contrib.auth.models import User


class UserSerializer (serializers.ModelSerializer):
   #Este metodo señala que solo se puede escribir la data y esta no va a ser devuelta
   #Se aconseja usarlo en metodos sensible
   password = serializers.CharField(write_only=True)
   class Meta:
      model = User
      fields = ['username', 'password', 'email', 'first_name', 'last_name']
      extra_kwargs = {
          'username': {'required': True},
          'password': {'required': True},
          'email': {'required': True},
          'first_name': {'required': True},
          'last_name': {'required': True},
          } 

   def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user