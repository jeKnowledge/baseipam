from django.contrib import admin

# Register your models here.
from siteBI.models import Content,Image,Portfolio,Testimony

class ContentAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        return False
    def has_delete_permission(self, request, obj=None):
        return False

class ImageAdmin(admin.ModelAdmin):
    pass

class TestimonyAdmin(admin.ModelAdmin):
    pass

admin.site.register(Content, ContentAdmin)
admin.site.register(Image, ImageAdmin)
admin.site.register(Portfolio, ImageAdmin)
admin.site.register(Testimony, TestimonyAdmin)
