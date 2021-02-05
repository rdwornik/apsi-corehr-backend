from django.contrib.auth.backends import BaseBackend
from django.core.exceptions import ValidationError

from users import models

class EmailAuthBackend(BaseBackend):
    r"""
    The EmailAuthBackend class inherits the base BaseBackend which is responsible for user authentication. As the default
    authentically consists of a username and password, as part of the application customization, the user can log in using an email instead of a username.
    """
    def authenticate(self, request, username=None, password=None):
        """
        The authenticate method belongs to the BaseBackend class and is used for authentication. It has been overwritten to replace the username with an email.
        """
        try:
            user = models.Employee.objects.get(email=username)
            
            if user.check_password(password):
                return user
            else:
                return None
        except models.Employee.DoesNotExist:
            raise ValidationError("Invalid credentials")

    def get_user(self, user_id):
        """
        This method returns user based on the id passed in the argument if user doesn't excist return None
        """
        try:
            return models.Employee.objects.get(pk=user_id)
        except models.Employee.DoesNotExist:
            return None