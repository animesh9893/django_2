from django.contrib import admin

# Register your models here.
from .models import User , SocialAccounts

admin.site.register(User)
admin.site.register(SocialAccounts)