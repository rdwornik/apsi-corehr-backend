from django.contrib.auth.backends import BaseBackend
from django.core.exceptions import ValidationError

from users import models

class EmailAuthBackend(BaseBackend):
    def authenticate(self, request, username=None, password=None):
        try:
            print(username)
            print(models.Employee.objects.all())
            user = models.Employee.objects.get(email=username)
            
            print(user)
            if user.check_password(password):
                return user
            else:
                return None
        except models.Employee.DoesNotExist:
            raise ValidationError("Invalid credentials")

    def get_user(self, user_id):
        try:
            return models.Employee.objects.get(pk=user_id)
        except models.Employee.DoesNotExist:
            return None