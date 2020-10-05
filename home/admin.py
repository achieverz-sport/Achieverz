from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.safestring import mark_safe
# Register your models here.
from .models import User
from .models import Group
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'is_organizer','mobile', 'date_joined', 'login_as')
    list_display_links = ('id', 'email')
    search_fields = ('email', 'mobile')
    list_filter = ('is_organizer','is_active')
    list_per_page = 50

    def login_as(self, obj):
        # Need to add dynamic Site URL here
        return mark_safe('<a href="/admin-login/home/user/login-as/%s/">Login</a>' % (obj.id))
    
    login_as.allow_tags = True
    login_as.short_description = 'Action'

    # def has_delete_permission(self, request, obj=None):
    #     return False

admin.site.register(User, UserAdmin)