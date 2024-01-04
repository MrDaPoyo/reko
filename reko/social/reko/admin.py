from django.contrib import admin
from django.contrib.auth.models import Group, User

# Unregister "Groups"
admin.site.unregister(Group)

# Extend User Model
class UserAdmin(admin.ModelAdmin):
    model = User
    # Display just username fields on "admin" page
    fields = ["username"]

admin.site.unregister(User)
admin.site.register(User, UserAdmin)