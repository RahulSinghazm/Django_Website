# -*- coding: utf-8 -*-
from django.contrib import admin
from .models import Contact,Carrers

class Contactadmin(admin.ModelAdmin):
    list_display = ['firstname', 'email', 'message','time']
    list_filter = ['time']
    class meta:
     model=Contact
class Carreradmin(admin.ModelAdmin):
    list_display = ['job_title', 'req_skills','contact_no','updated_time']
    list_filter = ['job_title','updated_time','job_id']
    class meta:
        model=Carrers

admin.site.register(Contact,Contactadmin)
admin.site.register(Carrers,Carreradmin)


# Register your models here.
