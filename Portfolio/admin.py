from django.contrib import admin
from .models import *


class PrjectsAdmin(admin.ModelAdmin):
    list_display = ('Title', 'date_added')
admin.site.register(Projects, PrjectsAdmin)

class DesignAdmin(admin.ModelAdmin):
    list_display = ('name', 'percentage')
admin.site.register(Design, DesignAdmin)

class DesignAdmin(admin.ModelAdmin):
    list_display = ('name', 'percentage')
admin.site.register(Developing, DesignAdmin)

class ExternalAdmin(admin.ModelAdmin):
    list_display = ('context', 'details')
admin.site.register(External, ExternalAdmin)


class ContactAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        return False
  
    list_display = ('name', 'email', 'date_send')
    
admin.site.register(Contact, ContactAdmin)