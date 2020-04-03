from django.contrib import admin
from django.contrib.admin.options import ModelAdmin
from myapp.models import Notice, Branch, Profile, Course, Contact



# Register your models here.
class NoticeAdmin(ModelAdmin):
    list_display = ["subject", "cr_date"]
    search_fields = ["subject", "msg"]
    list_filter = ["cr_date"]
    
admin.site.register(Notice, NoticeAdmin)
admin.site.register(Branch)
admin.site.register(Profile)
admin.site.register(Course)


class ContactAdmin(ModelAdmin):
    list_display = ["name", "cr_date"]
    search_fields = ["name", "email", "phone"]
    list_filter = ["cr_date"]
    
admin.site.register(Contact, ContactAdmin)