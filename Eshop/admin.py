from django.contrib import admin
from .models import *
# Register your models here.
admin.site.site_header="My Website | EshopProject "

class StudentAdmin(admin.ModelAdmin):
    #fields=["roll_no","email","name"]
    list_display=["name","roll_no","email","fee","gender","is_registered"]
    search_fields=["roll_no","name"]
    list_filter=["name","gender"]
    list_editable=["roll_no","email","fee","gender","is_registered"]

class Contact_UsAdmin(admin.ModelAdmin):
    #fields=["roll_no","email","name"]
    list_display=["id","name","contact_number","subject","message","added_on"]
    search_fields=["name"]
    list_filter=["name"]
    list_editable=["contact_number","subject"]

class CategoryAdmin(admin.ModelAdmin):
    #fields=["roll_no","email","name"]
    list_display=["id","cat_name","description","added_on"]
    list_editable=["cat_name"]

admin.site.register(Student,StudentAdmin)
admin.site.register(Contact_Us,Contact_UsAdmin)
admin.site.register(Category,CategoryAdmin)
admin.site.register(register_table)
admin.site.register(add_product)
