from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.

class PropertyLocation(models.Model):
    propertyId = models.IntegerField(blank=False, null=False)
    propertyName = models.CharField(max_length=200)
    address = models.CharField(max_length=100)
    roomNumber = models.CharField(max_length=30)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=30)
    zipCode = models.CharField(max_length=30)

    def __str__(self):
        return str(self.roomNumber)

WorkorderPriority = (
        ('low', "Low"),
        ('medium', "Medium"),
        ('high', "High"),
        ('critical', "Critical"),
)

class Workorder(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='workorders')
    roomNumber = models.ForeignKey(PropertyLocation, on_delete=models.CASCADE, related_name='workorders')
    woId = models.IntegerField(blank=False, null=False)
    woDescription = models.CharField(max_length=100, blank=False)
    woPriority = models.CharField(max_length=10,choices=WorkorderPriority, default='low')
    created_date = models.DateTimeField(default=timezone.now)
    woStartDate = models.DateTimeField(default=timezone.now)
    woEndDate = models.DateTimeField(null=True, blank=True, default=timezone.now)
    is_open = models.BooleanField(default=True, blank=False, null=False)

    def __str__(self):
        return str(self.woId)

class MaintenanceWork(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='maintenanceworks')
    woId = models.ForeignKey(Workorder, on_delete=models.CASCADE, related_name='maintenanceworks', default=999)
    mwId = models.IntegerField(blank=False, null=False)
    mwDescription = models.CharField(max_length=100, blank=False)
    mwWorkCost=models.IntegerField(blank=True, null=True)
    mwStartDateTime = models.DateTimeField()
    mwEndDateTime = models.DateTimeField(null=True, blank=True)
    is_open = models.BooleanField(default=True, blank=False, null=False)

    def __str__(self):
        return str(self.mwId)


class Equipment(models.Model):
    mwId = models.ForeignKey(MaintenanceWork, on_delete=models.CASCADE, related_name='equipments')
    equipId = models.IntegerField(blank=False, null=False)
    equipName = models.CharField(max_length=100, blank=False)
    equipDescription = models.CharField(max_length=200, blank=True)
    equipMaintCost=models.IntegerField(blank=True, null=True)
    equipUnitCost = models.IntegerField(blank=True, null=True)
    equipUnitStock = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return str(self.equipId)