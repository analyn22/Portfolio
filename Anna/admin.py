from django.contrib import admin
from .models import *

class PersonalAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        return False
    def has_delete_permission(self, request, obj=None):
        return False
admin.site.register(Personal,PersonalAdmin)
admin.site.register(Social)