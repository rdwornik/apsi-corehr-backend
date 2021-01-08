from django.contrib import admin

from corehr import models
# Register your models here.
admin.site.register(models.JobPosition)
admin.site.register(models.ContractType)
admin.site.register(models.Department)
admin.site.register(models.AbsenceType)
admin.site.register(models.OrganizationMembership)
admin.site.register(models.Organization)
admin.site.register(models.Managers)
admin.site.register(models.Contract)
admin.site.register(models.Absence)