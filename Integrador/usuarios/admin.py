from django.contrib import admin

# Register your models here.
from .models import Data_User,Activity_User,Election,Data_Election,Interaction_User,Activity_Report

admin.site.register(Data_User)
admin.site.register(Activity_User)

admin.site.register(Election)
admin.site.register(Data_Election)
admin.site.register(Interaction_User)

admin.site.register(Activity_Report)