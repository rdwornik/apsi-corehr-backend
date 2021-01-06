from django.db import models
from django.core.validators import RegexValidator
from django.utils.translation import ugettext as _
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
# Create your models here.

class MyEmployeeManager(BaseUserManager):
    """
    Employee manager needed
    """
    def create_user(self, name, surname, email, birthdate, phone_number, password=None, pesel=None):
        """
        Creates and saves a User with the given email, date of
        birth and password.        
        """
        #create user here
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
            name=name,
            surname=surname,
            birthdate=birthdate,
            phone_number=phone_number,
            pesel=pesel
        )

        user.set_password(password)
        user.save(using=self._db)
        return user
        

    def create_superuser(self, name, surname, email, birthdate, phone_number, password=None, pesel=None):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        user = self.create_user(
            name,
            surname,
            email,
            birthdate,
            phone_number,
            password,
            pesel
        )
        user.is_admin = True
        user.save(using=self._db)
        return user




class Employee(AbstractBaseUser, PermissionsMixin):
    """The most imprortant model in the aplication. It stores the user data."""

    name = models.TextField(_("Name"))
    surname = models.TextField(_("Surname"))
    email = models.EmailField(_("Email"), max_length=254, unique=True)
    pesel = models.CharField(_("Pesel"), max_length=11, validators=[RegexValidator(r'^\d{1,11}$')], blank=True, null=True, default=None)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone_number = models.CharField(_("Phone Number"), max_length=17, validators=[phone_regex])
    birthdate = models.DateField(_("Date"), auto_now=False, auto_now_add=False)

    job_position = models.ForeignKey("corehr.JobPosition", verbose_name=_("Job Position"), on_delete=models.CASCADE, default=1)

    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = MyEmployeeManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name', 'surname', 'phone_number', 'birthdate',]

    def __str__(self):
        """Unicode representation of Employee."""
        return "{0} {1} {2} {3} {4} {5}".format(self.name,
                                                        self.surname,
                                                        self.email,
                                                        self.pesel,
                                                        self.phone_number,
                                                        self.birthdate)
    
    def has_perm(self, perm, obj=None):
        """
        Method needed to create Abstact User
        """
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True
    
    def has_module_perms(self, app_label):
        """
        Method uneed to create Abstarct User
        """
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True


    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin