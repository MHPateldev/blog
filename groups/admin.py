from django.contrib import admin
from . import models
from posts.models import Post
# Register your models here.
class GroupMemberInline(admin.TabularInline):
    model = models.GroupMember

admin.site.register(models.Group)
admin.site.register(Post)
