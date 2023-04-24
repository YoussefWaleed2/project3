from django.db import models

from django.contrib.auth.models import User  



class Todo(models.Model):
    user = models.ForeignKey(User , on_delete = models.CASCADE , )
    title = models.CharField(max_length=150 , null=True  ,blank = True )
    dateCreated = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title 



class TodoItem(models.Model):
    title = models.CharField(max_length=150 , null=True  ,blank = True )
    description = models.TextField()
    is_completed = models.BooleanField(default=False)
    todo = models.ForeignKey(Todo , on_delete = models.CASCADE)


    def __str__(self):
        return self.title



