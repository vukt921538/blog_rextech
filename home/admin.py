from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from home.models import Profile, Post, CommentPost, Comment_to_comment
from shop.models import Product

# Register your models here.
class ProfileTabular(admin.TabularInline):
    model = Profile
    can_delete = False
    verbose_name_plural = 'profile'

class UserAdmin(BaseUserAdmin):
    inlines = [
        ProfileTabular
    ]
admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.register(Post)
admin.site.register(CommentPost)
admin.site.register(Comment_to_comment)
admin.site.register(Product)