from django.shortcuts import render

from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.tokens import RefreshToken
from django.conf import settings
from users.serializers import EmployeeSerializer
# Create your views here.
from users import models, serializers
from django.shortcuts import get_object_or_404
from rest_framework import filters
from rest_framework import generics
import jwt
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
        serializer.save()


    def filter_queryset(self, queryset):
        # Other condition for different filter backend goes here
        print("hello")
        for backend in list(self.filter_backends):
            queryset = backend().filter_queryset(self.request, queryset, view=self)
        return queryset


class BlacklistTokenUpdateView(APIView):
    permission_classes = [AllowAny]
    authentication_classes = ()

    def post(self, request):
        try:
            refresh_token = request.data["refresh_token"]
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response('logout',status=status.HTTP_205_RESET_CONTENT)
        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST)


class VerifyUser(generics.GenericAPIView):
    queryset = models.Employee.objects.all()

    def get(self, request):
        token = request.GET.get('token')
        print('payload ' + str(settings.SECRET_KEY))
        try:
            payload = jwt.decode(jwt=token, key=settings.SECRET_KEY, algorithms=['HS256'])
            print('payload 1 ' + str(payload))
            user = models.Employee.objects.get(id=payload['user_id'])
            if not user.is_active:
                user.is_active = True
                user.save()
            serializer = serializers.EmployeeSerializer(user)
            json = JSONRenderer().render(serializer.data)    
            return Response(user, status=status.HTTP_200_OK)
        except jwt.ExpiredSignatureError as e:
            return Response({'error': 'Activations link expired'}, status=status.HTTP_400_BAD_REQUEST)
        except jwt.exceptions.DecodeError as e:
            return Response({'error': 'Invalid Token'}, status=status.HTTP_400_BAD_REQUEST)