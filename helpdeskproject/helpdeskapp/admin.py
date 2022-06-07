from django.contrib import admin
from .models import AddTicket, InstallMent, Devices, OS_System, Status, Change_Device
from import_export.admin import ImportExportModelAdmin
# Register your models here.

admin.site.register(InstallMent)
admin.site.register(Devices)
admin.site.register(OS_System)
admin.site.register(Status)
admin.site.register(Change_Device)

@admin.register(AddTicket)
class AddticketAdmin(ImportExportModelAdmin):
    pass