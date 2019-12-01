from django.contrib import admin

# Register your models here.
from siteBI.models import Content

class ContentAdmin(admin.ModelAdmin):
    pass
admin.site.register(Content, ContentAdmin)
