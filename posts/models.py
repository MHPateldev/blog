from django.db import models
from django.urls import reverse
from django.conf import settings

import misaka

from groups.models import Group
# Create your models here.
#Posts models.py
from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model
User = get_user_model()

from django import template
register = template.Library()

class Post(models.Model):
    user = models.ForeignKey(User, related_name='posts', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now=True)
    message = models.TextField()
    message_html= models.TextField(editable=False)
    group = models.ForeignKey(Group, related_name='posts',null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.message

    def save(self,*args,**kwargs):
        self.message_html=  misaka.html(self.message)
        group = get_object_or_404(Group,name = self.group.name)
        if self.user in group.members.all():
            pass
        else :
            self.group = None 
        super().save(*args,**kwargs)
    
    def get_absolute_url(self):
        return reverse("posts:single", kwargs={"username": self.user.username, 'pk':self.pk})

    class Meta:
        ordering = ['-created_at']
        unique_together = ['user','message']