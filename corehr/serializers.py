from rest_framework import serializers
from corehr import models as corehr_models
from users import models as users_models
from users import serializers as users_serializers
from django.shortcuts import get_object_or_404
from django.forms.models import model_to_dict
from rest_framework.renderers import JSONRenderer

class OrganizationSerializer(serializers.ModelSerializer):
    '''
        Responsible for serializing Organization
    '''
    class Meta:
        model = corehr_models.Organization
        fields = '__all__'

class MemberEmployeeFieldSerializer(serializers.RelatedField):
    def to_representation(self, value):
        serializer = users_serializers.EmployeeSerializer(value)
        json = JSONRenderer().render(serializer.data)
        return json
    def to_internal_value(self, data):
        return get_object_or_404(users_models.Employee, pk=data)
    class Meta:
        model = users_models.Employee
    
class OrganizationFieldSerializer(serializers.RelatedField):
    def to_representation(self, value):
        serializer = OrganizationSerializer(value)
        json = JSONRenderer().render(serializer.data)
        return json
    def to_internal_value(self, data):
        return get_object_or_404(corehr_models.Organization, pk=data)
    class Meta:
        model = corehr_models.Organization

class OrganizationMembershipSerializer(serializers.ModelSerializer):
    '''
        Responsible for serializing OrganizationMembership
    '''
    member_employee = MemberEmployeeFieldSerializer(queryset=users_models.Employee.objects.all())
    organization = OrganizationFieldSerializer(queryset=corehr_models.Organization.objects.all())

    class Meta:
        model = corehr_models.OrganizationMembership
        fields = '__all__'

    def create(self, validated_data):
        member_employee_id = validated_data.pop('member_employee')
        member_employee_instance = get_object_or_404(users_models.Employee, pk=member_employee_id.pk)

        organization_id = validated_data.pop('organization')
        organization_instance = get_object_or_404(corehr_models.Organization, pk=organization_id.pk)

        return corehr_models.OrganizationMembership.objects.create(member_employee=member_employee_instance,organization=organization_instance)
        

class ManagerFieldSerializer(serializers.RelatedField):
    def to_representation(self, value):
        serializer = users_serializers.EmployeeSerializer(value)
        json = JSONRenderer().render(serializer.data)
        return json
    def to_internal_value(self, data):
        return get_object_or_404(users_models.Employee, pk=data)

    class Meta:
        model = users_models.Employee
    
class EmployeeFieldSerializer(serializers.RelatedField):
    def to_representation(self, value):
        serializer = users_serializers.EmployeeSerializer(value)
        json = JSONRenderer().render(serializer.data)
        return json
    def to_internal_value(self, data):
        return get_object_or_404(users_models.Employee, pk=data)
    class Meta:
        model = users_models.Employee

class ManagersSerializer(serializers.ModelSerializer):
    '''
        Responsible for serializing Managers
    '''
    manager = ManagerFieldSerializer(queryset=users_models.Employee.objects.all())
    employee = EmployeeFieldSerializer(queryset=users_models.Employee.objects.all())

    class Meta:
        model = corehr_models.Managers
        fields = '__all__'

    def create(self, validated_data):
        manager_id = validated_data.pop('manager')
        manager_instance = get_object_or_404(users_models.Employee, pk=manager_id.pk)

        employee_id = validated_data.pop('employee')
        employee_instance = get_object_or_404(users_models.Employee, pk=employee_id.pk)

        return corehr_models.Managers.objects.create(manager=manager_instance,employee=employee_instance)

#SŁOWNIK EASY
class JobPositionSerializer(serializers.ModelSerializer):
    '''
        Responsible for serializing JobPosition
    '''
    class Meta:
        model = corehr_models.JobPosition
        fields = '__all__'

#SŁOWNIK EAS
class ContractTypeSerializer(serializers.ModelSerializer):
    '''
        Responsible for serializing ContractType
    '''
    class Meta:
        model = corehr_models.ContractType
        fields = '__all__'

    
class ContractSerializer(serializers.ModelSerializer):
    '''
        Responsible for serializing Contract
    '''
    class Meta:
        model = corehr_models.Contract
        fields = '__all__'

class DepartmentSerializer(serializers.ModelSerializer):
    '''
        Responsible for serializing Department
    '''
    class Meta:
        model = corehr_models.Department
        fields = '__all__'

class AbsenceSerializer(serializers.ModelSerializer):
    '''
        Responsible for serializing Absence
    '''
    class Meta:
        model = corehr_models.Absence
        fields = '__all__'

class AbsenceTypeSerializer(serializers.ModelSerializer):
    '''
        Responsible for serializing AbsenceType
    '''
    class Meta:
        model = corehr_models.AbsenceType
        fields = '__all__'