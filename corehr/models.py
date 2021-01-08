from django.db import models
from django.core.validators import RegexValidator
from django.utils.translation import ugettext as _
# Create your models here.


class OrganizationMembership(models.Model):
    """Model definition for OrganizationMembership."""

    # TODO: Define fields here
    member_employee = models.ForeignKey("users.Employee", verbose_name=_("Employee"), on_delete=models.CASCADE,related_name='member_employee')
    organization = models.ForeignKey("corehr.Organization", verbose_name=_("Organization"), on_delete=models.CASCADE,related_name='organization')

    class Meta:
        """Meta definition for OrganizationMembership."""

        verbose_name = 'OrganizationMembership'
        verbose_name_plural = 'OrganizationMemberships'
        unique_together = ( 'member_employee',
                            'organization' )

    def __str__(self):
        """Unicode representation of OrganizationMembership."""
        return "{0} {1}".format(self.member_employee, self.organization)


class Organization(models.Model):
    """Model definition for Organization."""

    # TODO: Define fields here
    name = models.CharField(_("Organization"), max_length=256, default="None", unique=True)

    class Meta:
        """Meta definition for Organization."""

        verbose_name = 'Organization'
        verbose_name_plural = 'Organizations'
    
    def __str__(self):
        """Unicode representation of Organization."""
        return "{0}".format(self.name)



class Managers(models.Model):
    """Model definition for Managers."""

    # TODO: Define fields here
    manager = models.ForeignKey("users.Employee", verbose_name=_("Manager"), on_delete=models.CASCADE,related_name='manager')
    employee = models.ForeignKey("users.Employee", verbose_name=_("Employee"), on_delete=models.CASCADE,related_name='employee')
    class Meta:
        """Meta definition for Managers."""

        verbose_name = 'Managers'
        verbose_name_plural = 'Managers'
        unique_together = ( 'manager',
                            'employee')

    def __str__(self):
        """Unicode representation of Managers."""
        return "{0} {1}".format(self.manager, self.employee)

class JobPosition(models.Model):
    """Model definition for JobPosition."""
    name = models.CharField(_("Job Position"), max_length=256, default="None", unique=True)
    class Meta:
        """Meta definition for JobPosition."""

        verbose_name = 'JobPosition'
        verbose_name_plural = 'JobPositions'

    def __str__(self):
        """Unicode representation of JobPosition."""
        return "{0}".format(self.name)

class ContractType(models.Model):
    """Model definition for ContractType."""

    name = models.CharField(_("Contract Type"), max_length=256, default="None", unique=True)

    class Meta:
        """Meta definition for ContractType."""

        verbose_name = 'ContractType'
        verbose_name_plural = 'ContractTypes'

    def __str__(self):
        """Unicode representation of ContractType."""
        return "{0}".format(self.name)

class Contract(models.Model):
    """Model definition for Contract."""

    date_from = models.DateField(_("Date from"), auto_now=False, auto_now_add=False)
    date_to = models.DateField(_("Date to"), auto_now=False, auto_now_add=False)
    base_rate = models.DecimalField(_("Base rate"), max_digits=9, decimal_places=2)
    # post_code_regex = RegexValidator(
    #     regex=r'^(^[0-9]{2}(?:-[0-9]{3})?$)?$)',
    #     message=_(u'Must be valid zipcode in formats 12345 or 12-345'),
    # )
    post_code = models.CharField(_("Post code"), max_length=9)
    # file_name = models.FileField(_("File"), upload_to=None, max_length=100)
    file_name = models.CharField(_("File"), max_length=256)

    job_position = models.ForeignKey("corehr.JobPosition", verbose_name=_("Job Position"), on_delete=models.CASCADE)
    contract_type = models.ForeignKey("corehr.ContractType", verbose_name=_("Contract Type"), on_delete=models.CASCADE)
    department = models.ForeignKey("corehr.Department", verbose_name=_("Department"), on_delete=models.CASCADE)

    class Meta:
        """Meta definition for Contract."""

        verbose_name = 'Contract'
        verbose_name_plural = 'Contracts'
        unique_together = ( 'date_from',
                            'date_to',
                            'base_rate',
                            'post_code',
                            'file_name',
                            'job_position',
                            'contract_type',
                            'department'
                            )

    def __str__(self):
        """Unicode representation of Contract."""
        return "{0} {1} {2} {3} {4} {5} {6} {7}".format( 
                                                        self.date_from, 
                                                        self.date_to, 
                                                        self.base_rate, 
                                                        self.post_code,
                                                        self.file_name, 
                                                        self.job_position,
                                                        self.contract_type,
                                                        self.department )

class Department(models.Model):
    """Model definition for Department."""

    name = models.CharField(_("Department"), max_length=256, default="None", unique=True)

    class Meta:
        """Meta definition for Department."""

        verbose_name = 'Department'
        verbose_name_plural = 'Departments'

    def __str__(self):
        """Unicode representation of Department."""
        return "{0}".format(self.name)

class Absence(models.Model):
    """Model definition for Absence."""

    date_from = models.DateField(_("Date from"), auto_now=False, auto_now_add=False)
    date_to = models.DateField(_("Date to"), auto_now=False, auto_now_add=False)

    employee = models.ForeignKey("users.Employee", verbose_name=_(""), on_delete=models.CASCADE)
    absence_type = models.ForeignKey("corehr.AbsenceType", verbose_name=_(""), on_delete=models.CASCADE)

    class Meta:
        """Meta definition for Absence."""

        verbose_name = 'Absence'
        verbose_name_plural = 'Absences'
        unique_together = ( 'date_from',
                            'date_to',
                            'employee',
                            'absence_type')

    def __str__(self):
        """Unicode representation of Absence."""
        return "{0} {1} {2} {3}".format(self.date_from,
                                        self.date_to,
                                        self.employee,
                                        self.absence_type)

class AbsenceType(models.Model):
    """Model definition for AbsenceType."""

    name = models.CharField(_("Absence type"), max_length=256, default="None", unique=True)

    class Meta:
        """Meta definition for AbsenceType."""

        verbose_name = 'AbsenceType'
        verbose_name_plural = 'AbsenceTypes'

    def __str__(self):
        """Unicode representation of AbsenceType."""
        return "{0}".format(self.name)