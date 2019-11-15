from django.contrib import admin
from .models import Resident,MaintenanceWorker,Orc_Staff,Workorder,Equipment,MaintenanceWork,Roomallotment,User
from django.contrib.auth.admin import UserAdmin


admin.site.register(User, UserAdmin)

class ResidentList(admin.ModelAdmin):
    list_display = ( 'resident_id', 'resident_name')
    list_filter = ( 'resident_id', 'resident_name')
    search_fields = ('resident_id','resident_name')
    ordering = ['resident_id']

admin.site.register(Resident,ResidentList)

class MaintenanceWorkerList(admin.ModelAdmin):
    list_display = ( 'worker_id', 'maintenanceworker_name')
    list_filter = ( 'worker_id', 'maintenanceworker_name')
    search_fields = ('worker_id','maintenanceworker_name')
    ordering = ['worker_id']

admin.site.register(MaintenanceWorker,MaintenanceWorkerList)

class StaffList(admin.ModelAdmin):
    list_display = ( 'orc_staff_id', 'orc_staff_name')
    list_filter = ( 'orc_staff_id', 'orc_staff_name')
    search_fields = ('orc_staff_id','orc_staff_name')
    ordering = ['orc_staff_id']

admin.site.register(Orc_Staff,StaffList)


class WorkorderList(admin.ModelAdmin):
    list_display = ( 'workorder_Description', 'workorder_id')
    list_filter = ( 'workorder_Description', 'workorder_Description')
    search_fields = ('workorder_Description','workorder_Description')
    ordering = ['workorder_Description']

admin.site.register(Workorder,WorkorderList)


class EquipmentList(admin.ModelAdmin):
    list_display = ( 'equipment_id', 'equipment_name')
    list_filter = ( 'equipment_id', 'equipment_name')
    search_fields = ('equipment_id','equipment_name')
    ordering = ['equipment_id']

admin.site.register(Equipment,EquipmentList)

class MaintenanceworkList(admin.ModelAdmin):
    list_display = ( 'maintenancework_id','maintenancework_description')
    list_filter = ( 'maintenancework_id','maintenancework_description')
    search_fields = ('maintenancework_id','maintenancework_description')
    ordering = ['maintenancework_id']

admin.site.register(MaintenanceWork,MaintenanceworkList)

class RoomallotmentList(admin.ModelAdmin):
    list_display = ( 'property_number', 'resident_name')
    list_filter = ( 'property_number', 'resident_name')
    search_fields = ('property_number','resident_name')
    ordering = ['property_number']

admin.site.register(Roomallotment,RoomallotmentList)