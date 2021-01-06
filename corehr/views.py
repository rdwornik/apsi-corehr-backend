from django.shortcuts import render

from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.tokens import RefreshToken

from users.serializers import EmployeeSerializer
# Create your views here.
from users import models, serializers
from django.shortcuts import get_object_or_404
from rest_framework import filters


#TODO Filtery
#TODO zmiana hasła
#TODO CRUD DO POZYCJI DO KlUCZY
#TODO ADMIN zarejestruj te inne modele 
#Permission
#Szur->nie widzy innych szurów, Manager -> widzi szury + wyszukiwanie, Admin

#Stanowiska dodaje admin

class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = models.Employee.objects.all()
    serializer_class = serializers.EmployeeSerializer
    permission_classes = [AllowAny]
    # filter_backends = [filters.SearchFilter]
    filterset_fields = ('id', )

    def list(self, request):
        queryset = models.Employee.objects.all()
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
        serializer.save(owner=self.request.user)


    def filter_queryset(self, queryset):
        # Other condition for different filter backend goes here
        print("hello")
        for backend in list(self.filter_backends):
            queryset = backend().filter_queryset(self.request, queryset, view=self)
        return queryset