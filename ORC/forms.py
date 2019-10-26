from django import forms
from .models import Workorder,MaintenanceWork,Equipment,PropertyLocation

class WorkorderForm(forms.ModelForm):
    class Meta:
        model = Workorder
        fields = ('user', 'propertyId', 'woId', 'woDescription', 'woPriority', 'woStartDate', 'woEndDate')

class MaintenanceWorkForm(forms.ModelForm):
    class Meta:
        model = MaintenanceWork
        fields = ('mwId','mwDescription','mwStartDateTime','mwEndDateTime','mwWorkCost','user','woId')

class EquipmentForm(forms.ModelForm):
    class Meta:
        model = Equipment
        fields = ('mwId','equipId','equipName','equipDescription','equipMaintCost','equipUnitCost','equipUnitStock')

class PropertyForm(forms.ModelForm):
    class Meta:
        model = PropertyLocation
        fields = ('propertyId','propertyName','address','buildingNumber','city','state','zipCode')