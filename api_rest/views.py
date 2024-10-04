from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import User
from .serializers import UserSerializer

import json


@api_view(['GET']) # dizer pra api que a funcao abaixo so aceita o metodo GET 
def get_users(request): #define função get user 

    if request.method == 'GET':

        users = User.objects.all()                          # Get all objects in User's database (It returns a queryset)

        serializer = UserSerializer(users, many=True)       # Serialize the object data into json (Has a 'many' parameter cause it's a queryset)

        return Response(serializer.data)                    # Return the serialized data
    
    return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT'])
def get_by_nick(request, nick): #nick é a variável que o usuário digitou. 
    #nick é uma chave primária. vmaos ver no banco se corresponde
    try:
        user = User.objects.get(pk=nick) #se o usuário digitado for encontrado no banco de dados, ele será armazenado na variavel user
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)#se não encontrar, retornará que nao existe no bd
    
    if request.method == 'GET':
        serializer = UserSerializer(user) #cria uma instancia da classe UserSerializer que vai converter em formato JSON o que estiver dentro da variável USER. para que dessa forma seja tratado no frontend 
        return Response(serializer.data) # retorna os dados do user
    
    if request.method == 'PUT':

        serializer = UserSerializer(user, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)

        return Response(status=status.HTTP_400_BAD_REQUEST)



# CRUDZAO DA MASSA
@api_view(['GET','POST','PUT','DELETE'])
def user_manager(request): #cria função de gerenciamento 

# ACESSOS

    if request.method == 'GET':

        try:
            if request.GET['user']:                         # Check if there is a get parameter called 'user' (/?user=xxxx&...)

                user_nickname = request.GET['user']         # Find get parameter e armazena na variavel user_nickname

                try:
                    user = User.objects.get(pk=user_nickname)   # tenta encontrar no bd o nickname
                except:
                    return Response(status=status.HTTP_404_NOT_FOUND) #se não achar da um 404

                serializer = UserSerializer(user)           #cria um um serializer para o objeto user
                return Response(serializer.data)            # Retorna os dados do usuario serializados em formato JSON 

            else:
                return Response(status=status.HTTP_400_BAD_REQUEST)
                #se o parametro user nao for fornecido ele retorna um erro 
            
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    

# CRIANDO DADOS

    if request.method == 'POST':

        new_user = request.data #pega os dados enviados na requisição e coloca em new_user
        
        serializer = UserSerializer(data=new_user) #cria um serializer com os dados fornecidos

        if serializer.is_valid(): # verifica se os dados sao validos de acordo com as regras definidas no UserSerializer
            serializer.save() 
            return Response(serializer.data, status=status.HTTP_201_CREATED)
    
        return Response(status=status.HTTP_400_BAD_REQUEST) #se os dados não forem válidos retorna um 400

# EDITAR DADOS (PUT)

    if request.method == 'PUT':

        nickname = request.data['user_nickname'] #De toda a requisição, ele vai olhar apenas para o nickname. 

        try:
            updated_user = User.objects.get(pk=nickname) #busca no banco de dados pelo seu user
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)

        
        #print('Resultado final ', fn.soma(1,2))

        serializer = UserSerializer(updated_user, data=request.data) # Um serializer é criado para o usuário que foi encontrado (updated_user), e os novos dados enviados na requisição (request.data) são passados para ele. O serializer faz a validação e transformação dos dados recebidos para serem atualizados no banco.

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        
        return Response(status=status.HTTP_400_BAD_REQUEST)

