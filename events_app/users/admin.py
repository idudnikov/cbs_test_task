from django.contrib import admin

from .models import CustomUser as User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_filter = ('email',)
