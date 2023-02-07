from django.contrib import admin

# Register your models here.

from .models import User,Election,Data_Election,Interaction_User,Activity_Report

admin.site.register(User)
#admin.site.register(Activity_User)Activity_User

admin.site.register(Election)


admin.site.register(Data_Election)
admin.site.register(Interaction_User)

admin.site.register(Activity_Report)    