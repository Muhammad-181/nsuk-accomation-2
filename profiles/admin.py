from django.contrib import admin
from .forms import CustomUserChangeForm
from django.contrib.auth.forms import SetPasswordForm
from .models import User
from django.contrib import admin
from .forms import CustomUserChangeForm
from django.contrib.auth.admin import UserAdmin

# class UserAdminWithCustomFormn(admin.ModelAdmin):
#     form = CustomUserChangeForm
#     fields = ('last_login', 'superuser_status', 'groups', 'user_permission', 'username', 
#     'emial_address', 'staff_status', 'active', 'date_joined', 'first_name', 
#     'last_name',
#      'phone_number', 
#     'password', )
#     list_display = ('first_name', 'last_name', 'phone_number')

class CustomUserAdmin(UserAdmin):
    form = CustomUserChangeForm
    fieldsets = (
    (None, {'fields': ('username', 'password', 'phone_number', 'profile_picture', 'first_name', 'last_name', 'email', 'groups', 'user_permissions')}),
    ('Permissions', {'fields': ('is_staff', 'is_active', 'is_superuser', 'last_login', 'date_joined')}),
    )  
    def save_model(self, request, obj, form, change):
        # Save the provided password in hashed format
        obj.set_password(form.cleaned_data['password'])
        obj.save()


# class UserAdminWithDefaultForm(UserAdmin):
#     fields = ('first_name', 'last_name', 'phone_number')
#     list_display = ('first_name', 'last_name', 'phone_number')




# class MyAdmin(admin.ModelAdmin):
#     fields = ('first_name', 'last_name', 'phone_number', 'password')
#     list_display = ('first_name', 'last_name', 'phone_number')
    
admin.site.register(User, CustomUserAdmin)