from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.tokens import RefreshToken
from django.conf import settings
from users.serializers import EmployeeSerializer
from users import models, serializers
from django.shortcuts import get_object_or_404
from rest_framework import filters
from rest_framework import generics
import jwt
from rest_framework_simplejwt.backends import TokenBackend
from django.core.exceptions import ValidationError


class EmployeeViewSet(viewsets.ModelViewSet):
    r"""
    Class EmployeeViewSet is responsible for handling the REST API request to the server
    """
    queryset = models.Employee.objects.all()
    serializer_class = serializers.EmployeeSerializer
    permission_classes = [AllowAny]
    filterset_fields = ('id', )

    def list(self, request):
        r"""
        Thie method is responsible for getting all Employee objects in the database and deserializing them to the form of JSON list 
        """
        queryset = models.Employee.objects.all()
        serializer = self.serializer_class(self.filter_queryset(self.get_queryset()), many=True, context={"request": request})

        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        r"""
        This method is responsible for retriving the single user by id
        """
        user = get_object_or_404(self.queryset, pk=pk)
        serializer = self.serializer_class(user)
        return Response(serializer.data)
    
    def create(self, request, *args, **kwargs):
        r"""
        This method is responsible for creating the user. It also validates if the data send in POST request are in correct format  
        """
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def destroy(self, request, *args, **kwargs):
        r"""
        This method is responsible for deleting the Employee instance in database
        """
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)

    def update(self, request, *args, **kwargs):
        r"""
        This method is responsible for updating Employee data in database.
        """
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)
    
    def partial_update(self, request, *args, **kwargs):
        r"""
        This method is responsible for partial update
        """
        kwargs['partial'] = True
        return self.update(request, *args, **kwargs)

    def perform_create(self, serializer):
        r"""
        This method is responsible saving the serialized Employee object in database
        """
        serializer.save()


    def filter_queryset(self, queryset):
        r"""
           This method is responsible for handling the filter conditions defined in the query parameters.
           Other condition for different filter backend goes here.
        """
        for backend in list(self.filter_backends):
            queryset = backend().filter_queryset(self.request, queryset, view=self)
        return queryset


class BlacklistTokenUpdateView(APIView):
    r"""
    Class BlacklistTokenUpdateView is responsible for handling the REST API request for retriving the token for the Employee. 
    """

    permission_classes = [AllowAny]
    authentication_classes = ()

    def post(self, request):
        r"""
        This method handles the POST request made to the server when users logsout from the webiste. The API retrives the token assined to the user and
        puts it on blaclkist when he logs out.
        """
        try:
            refresh_token = request.data["refresh_token"]
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response('logout',status=status.HTTP_205_RESET_CONTENT)
        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST)


class VerifyUser(generics.GenericAPIView):
    r"""
    Class is responsible for veryfing if the user has valid token.
    """
    
    queryset = models.Employee.objects.all()

    def get(self, request):
        r"""
        This method handles the get request with token assigned to the user and checks if the token is valid. 
        """
        token = request.META.get('HTTP_AUTHORIZATION', " ").split(' ')[1]
        data = {'token': token}
        try:
            valid_data = TokenBackend(algorithm='HS256').decode(token,verify=False)
            user = valid_data['user']
            request.user = user
        except ValidationError as v:
            print("validation error", v)