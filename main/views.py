from django.shortcuts import render , redirect
from django.http import HttpResponse
from .models import Todo , TodoItem
from .decorators import unathintecatedusers
# django.contrib
from django.contrib.auth import authenticate , login , logout

from django.contrib.auth.decorators import login_required

from django.contrib.auth.forms import UserCreationForm
from .forms import UserForm ,TodoForm


                        
@login_required(login_url='login')
def home(request):
    if request.user :
        todos = Todo.objects.filter(user = request.user)
       
    else:
        return redirect('login')
    context = {
        "todos":todos,
        "user":request.user,
      
    }

    return render( request , 'home.html' , context) 



@unathintecatedusers
def register(request):
  
        form = UserForm()
        if request.method =="POST":
            form = UserForm(request.POST)
            if form.is_valid:
                form.save()
                return redirect("login")
        context=  {
            "form":form ,
        }
        return render(request, 'register.html' , context)


@unathintecatedusers
def userLogin(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        print(username)
        user = authenticate(username = username , password = password)
        print(user)
        if user is not None :
            login(request , user)
            return redirect('home')
        
        else:
            print("error")
    context={
        
    }
    return render(request , 'login.html' , context)





def logoutuser(request):
    
    logout(request)
    return redirect('home')



@login_required(login_url='login')
def createTodo(request):
    user = request.user 
    form = TodoForm()
    if request.method =="POST":
        form = TodoForm(request.POST)
        if form.is_valid :
          
            todo = form.save(commit=False)
            todo.user = user
            todo.save()
            return redirect('home')
            
    
    context = {
        
        "form":form ,
    }
    return render(request , 'createtodo.html' , context)



@login_required(login_url='login')
def createItem(request , id):
    todo = Todo.objects.get(id = id)
    if request.method =="POST":
        title = request.POST.get("title")
        description = request.POST.get("description")  
        item = TodoItem.objects.create( todo = todo ,title = title , description = description) 
        item.save()
        return redirect('home')    
    context = {
            
    }
    return render(request , "createitem.html" , context)

@login_required(login_url='login')
def detailed(request,id):
    todoitem = TodoItem.objects.get(id =id)
    context={
        "todoitem":todoitem
    }
    return render(request,'detailed.html',context)


def completed(request , id):
    todoitem = TodoItem.objects.get(id=id)
    todoitem.is_completed = True 
    todoitem.save()
    return redirect('home')