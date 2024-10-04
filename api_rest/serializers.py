#converter para json dos modelos
from rest_framework import serializers

#import o modelo que criamos
from .models import User, UserTasks

#criar uma classe 
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
        


#se fosse escolher os campos que desejo retornar 
#class UserSerializer(serializers.ModelSerializer):
#    class Meta:
#        model = User
#       fields = ['user_nickname', 'user_task']
 