"""User admin classes"""
# https://docs.djangoproject.com/en/3.2/ref/contrib/admin/
# https://docs.djangoproject.com/en/3.2/topics/auth/customizing/#extending-the-existing-user-model


# Django
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

# Models 
from django.contrib.auth.models import User
from users.models import Profile

# Register your models here for allow a model visible in site administration.
# admin.site.register(Profile)

# replace
@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    """Profile in site admin. With this
    class help a modify the ui in site admin"""

    list_display = ('id', 'user', 'phone_number', 'website', 'picture')
    list_display_links = ('id', 'user')
    list_editable = ('phone_number', 'website', 'picture')

    # create a search for fields in a list of profiles
    search_fields = ('user__email', 'user__first_name', 'user__last_name', 'phone_number')

    # create a column with filters
    list_filter = ('created', 'modified', 'user__is_active', 'user__is_staff')

    # views into profile

    fieldsets = (
        ('Profile', {
                'fields': (('user', 'picture'),),
            }
        ),
        ('Extra info',{
                'fields': (('website', 'phone_number'),
                            ('biography')
                )
            }
        ),
        ('Metadata',{
                'fields': (('created','modified'),),
            }
        )
    )

    # define field with permission read only 
    readonly_fields = ('created', 'modified',)


# Define an inline admin descriptor for Profile model
class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False
    verbose_name_plural = 'profiles'


class UserAdmin(BaseUserAdmin):
    """Add profile admin to base user admin"""

    inlines = (ProfileInline,)
    list_display = (
        'username',
        'email',
        'first_name',
        'last_name',
        'is_active',
        'is_staff'
    )

# unregister user model , and update the user model with new ui
admin.site.unregister(User)
admin.site.register(User, UserAdmin)

