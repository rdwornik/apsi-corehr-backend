from rest_framework import serializers
from users.models import Employee


class EmployeeSerializer(serializers.ModelSerializer):
    '''
        Responsible for serializing
    '''
    class Meta:
        model = Employee
        fields = ('id','email','name', 'surname', 'phone_number', 'birthdate', 'pesel', 'password')
        # extra_kwargs = {'password': {'write_only': True}}
    
    def create(self, validated_data):
        """
        docstring
        """
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance

class PasswordSerializer(serializers.Serializer):
    """
    Serializer for password change endpoint.
    """
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)