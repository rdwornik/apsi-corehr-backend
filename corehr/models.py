from django.db import models
from django.core.validators import RegexValidator
from django.utils.translation import ugettext as _
# Create your models here.


class JobPosition(models.Model):
    """Model definition for JobPosition."""
    name = models.CharField(_("Name"), max_length=256)
    manager = models.CharField(_("Manager"), max_length=256)
    employee = models.ForeignKey("users.Employee", verbose_name=_("Employee"), on_delete=models.CASCADE)
    
    class Meta:
        """Meta definition for JobPosition."""

        verbose_name = 'JobPosition'
        verbose_name_plural = 'JobPositions'

    def __str__(self):
        """Unicode representation of JobPosition."""
        pass

class ContractType(models.Model):
    """Model definition for ContractType."""

    models.CharField(_("Name"), max_length=256)

    class Meta:
        """Meta definition for ContractType."""

        verbose_name = 'ContractType'
        verbose_name_plural = 'ContractTypes'

    def __str__(self):
        """Unicode representation of ContractType."""
        pass

class Contract(models.Model):
    """Model definition for Contract."""

    date_from = models.DateField(_("Date from"), auto_now=False, auto_now_add=False)
    date_to = models.DateField(_("Date to"), auto_now=False, auto_now_add=False)
    base_rate = models.DecimalField(_("Base rate"), max_digits=9, decimal_places=2)
    post_code_regex = RegexValidator(
        regex=r'^(^[0-9]{2}(?:-[0-9]{3})?$)?$)',
        message=_(u'Must be valid zipcode in formats 12345 or 12-345'),
    )
    post_code = models.CharField(_("Post code"), max_length=9, validators=[post_code_regex])
    file_name = models.FileField(_("File"), upload_to=None, max_length=100)

    job_postion = models.ForeignKey("corehr.JobPosition", verbose_name=_(""), on_delete=models.CASCADE)
    contract_type = models.ForeignKey("corehr.ContractType", verbose_name=_(""), on_delete=models.CASCADE)
    department = models.ForeignKey("corehr.Department", verbose_name=_(""), on_delete=models.CASCADE)

    class Meta:
        """Meta definition for Contract."""

        verbose_name = 'Contract'
        verbose_name_plural = 'Contracts'

    def __str__(self):
        """Unicode representation of Contract."""
        pass

class Department(models.Model):
    """Model definition for Department."""

    models.CharField(_("Department"), max_length=256)

    class Meta:
        """Meta definition for Department."""

        verbose_name = 'Department'
        verbose_name_plural = 'Departments'

    def __str__(self):
        """Unicode representation of Department."""
        pass

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

    def __str__(self):
        """Unicode representation of Absence."""
        pass

class AbsenceType(models.Model):
    """Model definition for AbsenceType."""

    name = models.CharField(_("Absence type"), max_length=256)

    class Meta:
        """Meta definition for AbsenceType."""

        verbose_name = 'AbsenceType'
        verbose_name_plural = 'AbsenceTypes'

    def __str__(self):
        """Unicode representation of AbsenceType."""
        pass