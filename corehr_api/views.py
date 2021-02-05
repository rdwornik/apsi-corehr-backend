from django.shortcuts import render

from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.tokens import RefreshToken


# Create your views here.
from corehr import models, serializers
from django.shortcuts import get_object_or_404
from rest_framework import filters


class OrganizationMembershipViewSet(viewsets.ModelViewSet):
    r"""
    Class EmployeeViewSet is responsible for handling the REST API request to the server
    """

    queryset = models.OrganizationMembership.objects.all()
    serializer_class = serializers.OrganizationMembershipSerializer
    permission_classes = [AllowAny]
    filterset_fields = ('id', )

    def list(self, request):
        serializer = self.serializer_class(self.filter_queryset(self.get_queryset()), many=True, context={"request": request})
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        user = get_object_or_404(self.queryset, pk=pk)
        serializer = self.serializer_class(user)
        return Response(serializer.data)
    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)
    
    def partial_update(self, request, *args, **kwargs):
        kwargs['partial'] = True
        return self.update(request, *args, **kwargs)

    def perform_create(self, serializer):
        serializer.save()

    def filter_queryset(self, queryset):
        # Other condition for different filter backend goes here
        for backend in list(self.filter_backends):
            queryset = backend().filter_queryset(self.request, self.get_queryset(), view=self)
        return queryset

class OrganizationViewSet(viewsets.ModelViewSet):
    r"""
    Class OrganizationViewSet is responsible for handling the REST API request to the server
    """
    queryset = models.Organization.objects.all()
    serializer_class = serializers.OrganizationSerializer
    permission_classes = [AllowAny]
    filterset_fields = ('id', )  

    def list(self, request):
        serializer = self.serializer_class(self.filter_queryset(self.get_queryset()), many=True, context={"request": request})
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        user = get_object_or_404(self.queryset, pk=pk)
        serializer = self.serializer_class(user)
        return Response(serializer.data)
    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)
    
    def partial_update(self, request, *args, **kwargs):
        kwargs['partial'] = True
        return self.update(request, *args, **kwargs)

    def perform_create(self, serializer):
        serializer.save()

    def filter_queryset(self, queryset):
        # Other condition for different filter backend goes here
        for backend in list(self.filter_backends):
            queryset = backend().filter_queryset(self.request, self.get_queryset(), view=self)
        return queryset
class ManagersViewSet(viewsets.ModelViewSet):
    r"""
    Class ManagersViewSet is responsible for handling the REST API request to the server
    """
    queryset = models.Managers.objects.all()
    serializer_class = serializers.ManagersSerializer
    permission_classes = [AllowAny]
    filterset_fields = ('id', )  

    def list(self, request):
        serializer = self.serializer_class(self.filter_queryset(self.get_queryset()), many=True, context={"request": request})
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        user = get_object_or_404(self.queryset, pk=pk)
        serializer = self.serializer_class(user)
        return Response(serializer.data)
    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)
    
    def partial_update(self, request, *args, **kwargs):
        kwargs['partial'] = True
        return self.update(request, *args, **kwargs)

    def perform_create(self, serializer):
        serializer.save()

    def filter_queryset(self, queryset):
        # Other condition for different filter backend goes here
        for backend in list(self.filter_backends):
            queryset = backend().filter_queryset(self.request, self.get_queryset(), view=self)
        return queryset

class JobPositionViewSet(viewsets.ModelViewSet):
    r"""
    Class JobPositionViewSet is responsible for handling the REST API request to the server
    """
    queryset = models.JobPosition.objects.all()
    serializer_class = serializers.JobPositionSerializer
    permission_classes = [AllowAny]
    filterset_fields = ('id', )  

    def list(self, request):
        serializer = self.serializer_class(self.filter_queryset(self.get_queryset()), many=True, context={"request": request})
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        obj = get_object_or_404(self.queryset, pk=pk)
        serializer = self.serializer_class(obj)
        return Response(serializer.data)
    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)
    
    def partial_update(self, request, *args, **kwargs):
        kwargs['partial'] = True
        return self.update(request, *args, **kwargs)

    def perform_create(self, serializer):
        serializer.save()

    def filter_queryset(self, queryset):
        # Other condition for different filter backend goes here
        for backend in list(self.filter_backends):
            queryset = backend().filter_queryset(self.request, self.get_queryset(), view=self)
        return queryset

class ContractTypeViewSet(viewsets.ModelViewSet):
    r"""
    Class ContractTypeViewSet is responsible for handling the REST API request to the server
    """
    queryset = models.ContractType.objects.all()
    serializer_class = serializers.ContractTypeSerializer
    permission_classes = [AllowAny]
    filterset_fields = ('id', )  

    def list(self, request):
        serializer = self.serializer_class(self.filter_queryset(self.get_queryset()), many=True, context={"request": request})
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        obj = get_object_or_404(self.queryset, pk=pk)
        serializer = self.serializer_class(obj)
        return Response(serializer.data)
    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)
    
    def partial_update(self, request, *args, **kwargs):
        kwargs['partial'] = True
        return self.update(request, *args, **kwargs)

    def perform_create(self, serializer):
        serializer.save()

    def filter_queryset(self, queryset):
        # Other condition for different filter backend goes here
        for backend in list(self.filter_backends):
            queryset = backend().filter_queryset(self.request, self.get_queryset(), view=self)
        return queryset

class ContractViewSet(viewsets.ModelViewSet):
    r"""
    Class ContractViewSet is responsible for handling the REST API request to the server
    """
    queryset = models.Contract.objects.all()
    serializer_class = serializers.ContractSerializer
    permission_classes = [AllowAny]
    filterset_fields = ('id', )  

    def list(self, request):
        serializer = self.serializer_class(self.filter_queryset(self.get_queryset()), many=True, context={"request": request})
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        obj = get_object_or_404(self.queryset, pk=pk)
        serializer = self.serializer_class(obj)
        return Response(serializer.data)
    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)
    
    def partial_update(self, request, *args, **kwargs):
        kwargs['partial'] = True
        return self.update(request, *args, **kwargs)

    def perform_create(self, serializer):
        serializer.save()

    def filter_queryset(self, queryset):
        # Other condition for different filter backend goes here
        for backend in list(self.filter_backends):
            queryset = backend().filter_queryset(self.request, self.get_queryset(), view=self)
        return queryset
class DepartmentViewSet(viewsets.ModelViewSet):
    r"""
    Class DepartmentViewSet is responsible for handling the REST API request to the server
    """
    queryset = models.Department.objects.all()
    serializer_class = serializers.DepartmentSerializer
    permission_classes = [AllowAny]
    filterset_fields = ('id', )  

    def list(self, request):
        serializer = self.serializer_class(self.filter_queryset(self.get_queryset()), many=True, context={"request": request})
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        obj = get_object_or_404(self.queryset, pk=pk)
        serializer = self.serializer_class(obj)
        return Response(serializer.data)
    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)
    
    def partial_update(self, request, *args, **kwargs):
        kwargs['partial'] = True
        return self.update(request, *args, **kwargs)

    def perform_create(self, serializer):
        serializer.save()

    def filter_queryset(self, queryset):
        # Other condition for different filter backend goes here
        for backend in list(self.filter_backends):
            queryset = backend().filter_queryset(self.request, self.get_queryset(), view=self)
        return queryset

class AbsenceViewSet(viewsets.ModelViewSet):
    r"""
    Class AbsenceViewSet is responsible for handling the REST API request to the server
    """
    queryset = models.Absence.objects.all()
    serializer_class = serializers.AbsenceSerializer
    permission_classes = [AllowAny]
    filterset_fields = ('id', )

    def list(self, request):
        serializer = self.serializer_class(self.filter_queryset(self.get_queryset()), many=True, context={"request": request})
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        obj = get_object_or_404(self.queryset, pk=pk)
        serializer = self.serializer_class(obj)
        return Response(serializer.data)
    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)
    
    def partial_update(self, request, *args, **kwargs):
        kwargs['partial'] = True
        return self.update(request, *args, **kwargs)

    def perform_create(self, serializer):
        serializer.save()

    def filter_queryset(self, queryset):
        # Other condition for different filter backend goes here
        for backend in list(self.filter_backends):
            queryset = backend().filter_queryset(self.request, self.get_queryset(), view=self)
        return queryset

class AbsenceTypeViewSet(viewsets.ModelViewSet):
    r"""
    Class AbsenceTypeViewSet is responsible for handling the REST API request to the server
    """
    queryset = models.AbsenceType.objects.all()
    serializer_class = serializers.AbsenceTypeSerializer
    permission_classes = [AllowAny]
    filterset_fields = ('id', )  

    def list(self, request):
        serializer = self.serializer_class(self.filter_queryset(self.get_queryset()), many=True, context={"request": request})
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        obj = get_object_or_404(self.queryset, pk=pk)
        serializer = self.serializer_class(obj)
        return Response(serializer.data)
    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)
    
    def partial_update(self, request, *args, **kwargs):
        kwargs['partial'] = True
        return self.update(request, *args, **kwargs)

    def perform_create(self, serializer):
        serializer.save()

    def filter_queryset(self, queryset):
        # Other condition for different filter backend goes here
        for backend in list(self.filter_backends):
            queryset = backend().filter_queryset(self.request, self.get_queryset(), view=self)
        return queryset