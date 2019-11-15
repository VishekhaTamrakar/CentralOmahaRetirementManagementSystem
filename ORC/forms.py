from django import forms
from .models import Resident,MaintenanceWorker,Orc_Staff,Equipment,MaintenanceWork,Roomallotment

class ResidentForm(forms.ModelForm):
    class Meta:
        model = Resident
        fields = ('resident_id', 'resident_name', 'resident_occupation', 'resident_emailaddress','resident_marital_status', 'resident_familymember_count','resident_petdetails','resident_contactdetails','resident_startdate', 'resident_enddate')


class MaintenanceworkerForm(forms.ModelForm):
    class Meta:
        model = MaintenanceWorker
        fields = ('worker_id', 'maintenanceworker_name', 'worker_emailaddress', 'worker_address','worker_yearsofexperience','worker_contactdetails','workerstartdate','worker_enddate')


class Orc_Staff(forms.ModelForm):
    class Meta:
        model = Orc_Staff
        fields = ('orc_staff_id', 'orc_staff_name', 'orc_staff_emailaddress', 'orc_staff_address','orc_staff_yearsofexperience', 'orc_staff_contactdetails','orc_staff_position','orc_staff_startdate','orc_staff_enddate')


class Workorder(forms.ModelForm):
    class Meta:
        model = Workorder
        fields = ('resident_name', 'workorder_id', 'workorder_Description', 'workorder_category','workorder_priority','property_number', 'workorder_opendate','workorder_duedate','workorder_closedate','is_open')


class Equipment(forms.ModelForm):
    class Meta:
        model = Equipment
        fields = ('equipment_id', 'equipment_serialnumber', 'equipment_name', 'equipment_description','is_available','equipment_cost','equipment_purchasedate')

class MaintenanceWork(forms.ModelForm):
    class Meta:
        model = MaintenanceWork
        fields = ('maintenancework_id','maintenancework_description', 'workorder_id','maintenanceworker_name','property_number','equipment_name','maintenancework_cost','maintenancework_opendate','maintenancework_duedate','is_open','maintenancework_closedate')

class Roomallotment(forms.ModelForm):
    class Meta:
        model = Roomallotment
        fields = ('allotment_id', 'resident_name', 'property_number', 'property_floor','allotment_startdate','allotment_enddate')