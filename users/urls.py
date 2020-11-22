from django.urls import path
from .views import EmployeeUserCreate, BlacklistTokenUpdateView

app_name = 'users'

urlpatterns = [
    path('create/', EmployeeUserCreate.as_view(), name="create_user"),
    path('logout/blacklist/', BlacklistTokenUpdateView.as_view(),
         name='blacklist')
]