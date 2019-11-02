from django.contrib import admin
from .models import *

# Register your models here.
class PropertyLocationList(admin.ModelAdmin):
    list_display = ( 'roomNumber', 'propertyName' )
    list_filter = ( 'roomNumber', 'propertyName')
    search_fields = ('roomNumber', )
    ordering = ['roomNumber']

class MaintenanceWorkList(admin.ModelAdmin):
    list_display = ( 'mwId', 'mwDescription','woId' )
    list_filter = ( 'mwId', 'mwDescription','woId')
    search_fields = ('mwId', )
    ordering = ['mwId']

class WorkorderList(admin.ModelAdmin):
    list_display = ( 'woId', 'woDescription', 'woPriority' )
    list_filter = ( 'woId', 'woDescription', 'woPriority')
    search_fields = ('woId', )
    ordering = ['woId']

class EquipmentList(admin.ModelAdmin):
    list_display = ( 'equipId', 'equipName' )
    list_filter = ( 'equipId', 'equipName')
    search_fields = ('equipId', )
    ordering = ['equipId']

admin.site.register(PropertyLocation, PropertyLocationList)
admin.site.register(MaintenanceWork, MaintenanceWorkList)
admin.site.register(Workorder, WorkorderList)
admin.site.register(Equipment, EquipmentList)