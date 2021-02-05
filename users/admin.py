from django import forms
from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.core.exceptions import ValidationError

from users.models import Employee
# Register your models here.

class EmployeeCreationForm(forms.ModelForm):
    """The EmployeeCreationForm class is responsible for generating the form for creating an Employee in the administrator view"""

    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)
    
    class Meta:
        """Metadata for the EmployeeCreationForm class"""

        model = Employee
        fields = ('email','name', 'surname', 'phone_number', 'birthdate','pesel',)

    def clean_password2(self):
        """ Check that the two password entries match"""
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        """Save the provided password in hashed format"""
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user

class EmployeeChangeForm(forms.ModelForm):
    """The EmployeeChangeForm class is responsible for generating the form for editing in the administrator panel"""
    password = ReadOnlyPasswordHashField()

    class Meta:
        """Meta definition for EmployeeChangeform."""

        model = Employee
        fields = ('email', 'password', 'name', 'surname', 'phone_number', 'birthdate', 'pesel', 
        'is_active', 'is_admin')

    def clean_password(self):
        """ Regardless of what the user provides, return the initial value.
        This is done here, rather than on the field, because the
         field does not have access to the initial value"""
        return self.initial["password"]


class EmployeeAdmin(BaseUserAdmin):
    """
    The EmployeeAdmin class is a class representing Procownik in the admin panel
    """
    
    """ The forms to add and change user instances
    """
    form = EmployeeChangeForm
    add_form = EmployeeCreationForm

    """The fields to be used in displaying the User model.
    hese override the definitions on the base UserAdmin
     that reference specific fields on auth.User.
     """

    list_display = ('email', 'name', 'surname', 'phone_number', 'birthdate', 'pesel'
    , 'is_admin')
    list_filter = ('is_admin',)
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('name', 'surname', 'phone_number', 'birthdate', 'pesel')}),
        ('Permissions', {'fields': ('is_admin',)}),
    )
    
    """ add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    overrides get_fieldsets to use this attribute when creating a user.
    """
    
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'name', 'surname', 'phone_number', 'birthdate', 'pesel', 'password1', 'password2'),
        }),
    )
    search_fields = ('email', 'name', 'surname', 'phone_number', 'birthdate',)
    ordering = ('email', 'name', 'surname', 'phone_number', 'birthdate', 'pesel')
    filter_horizontal = ()




# Now register the new UserAdmin...
admin.site.register(Employee, EmployeeAdmin)
# ... and, since we're not using Django's built-in permissions,
# unregister the Group model from admin.
# admin.site.unregister(Group)