from django.db import models

#cria classe chamada user | models (django BD)
class User(models.Model):
    
    # campos que estarão dentro do nosso banco de dados 
    user_nickname = models.CharField(primary_key=True, max_length=100, default='')
    user_name = models.CharField(max_length=150, default='')
    user_email = models.EmailField(default='')
    user_age = models.IntegerField(default=0)

    #Método mágico: quando chamar qualquer função, ela tbm será chamada
    def __str__(self):
        return f'Nickname: {self.user_nickname} | E-mail: {self.user_email}'





class UserTasks(models.Model):
    user_nickname = models.CharField(max_length=100, default='')
    user_task = models.CharField(max_length=255, default='')