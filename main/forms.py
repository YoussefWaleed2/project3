from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from .models import Todo
class UserForm(UserCreationForm):
    class Meta:
        model  = User
        fields = ["username" , "email" , "password1" , "password2"]



class TodoForm(ModelForm):
    class Meta :
        model = Todo 
        fields =  '__all__'   
        exclude = ["user"]    