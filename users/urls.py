from django.urls import path
from .views import EmployeeUserCreate, BlacklistTokenUpdateView, EmployeeViewSet

app_name = 'users'

employee_list = EmployeeViewSet.as_view({
    'get': 'list',
    'post': 'create'
})
employee_detail = EmployeeViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})


urlpatterns = [
    path('employees/', employee_list, name='employee-list'),
    path('employees/<int:pk>/', employee_detail, name='employee-detail'),
    path('logout/blacklist/', BlacklistTokenUpdateView.as_view(),
         name='blacklist')
]