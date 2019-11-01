from django import forms
from .models import Workorder,MaintenanceWork,Equipment,PropertyLocation

class DateTimeInput(forms.DateTimeInput):
    input_type = 'date'

class WorkorderForm(forms.ModelForm):
    class Meta:
        model = Workorder
        fields = ('user', 'roomNumber', 'woId', 'woDescription', 'woPriority', 'woStartDate', 'woEndDate','is_open')
        widgets = {
            'woStartDate': DateTimeInput(),
            'woEndDate': DateTimeInput(),
        }

class MaintenanceWorkForm(forms.ModelForm):
    class Meta:
        model = MaintenanceWork
        fields = ('mwId','woId', 'mwDescription','mwWorkCost','user','mwStartDateTime','mwEndDateTime','is_open')

class EquipmentForm(forms.ModelForm):
    class Meta:
        model = Equipment
        fields = ('mwId','equipId','equipName','equipDescription','equipMaintCost','equipUnitCost','equipUnitStock')

class PropertyForm(forms.ModelForm):
    class Meta:
        model = PropertyLocation
        fields = ('propertyId','propertyName','address','roomNumber','city','state','zipCode')