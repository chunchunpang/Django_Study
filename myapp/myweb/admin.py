from django.contrib import admin
from myweb.models import Users
# Register your models here.
class UsersAdmin(admin.ModelAdmin):
    list_display=['title','body','timestart']

admin.site.register(Users,UsersAdmin)