from django.urls import path 
from . import views

urlpatterns = [
    path('' , views.home , name= "home"),
    
    path('register/' , views.register , name= "register"),
    path('login/' , views.userLogin , name= "login"),
    path("logout/" , views.logoutuser , name="logout"),
    
    
    path('createtodo/' ,views.createTodo , name = "createtodo"),
    path('createitem/<str:id>' ,views.createItem , name = "createitem")
    ,path('detailed/<str:id>' ,views.detailed ,name = "detailed")
    
    
    ,path('completed/<str:id>' , views.completed , name="completed")
]

