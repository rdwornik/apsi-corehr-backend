
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from rest_framework.routers import DefaultRouter
from users import views as users_views
from corehr_api import views as corehr_api_views
from rest_framework.routers import SimpleRouter

users_router = DefaultRouter()
users_router.register(r'employees', users_views.EmployeeViewSet)

corehr_router = DefaultRouter()
corehr_router.register(r'organizationmembership', corehr_api_views.OrganizationMembershipViewSet)
corehr_router.register(r'organization', corehr_api_views.OrganizationViewSet)
corehr_router.register(r'managers', corehr_api_views.ManagersViewSet)
corehr_router.register(r'jobposition', corehr_api_views.JobPositionViewSet)
corehr_router.register(r'contracttype', corehr_api_views.ContractTypeViewSet)
corehr_router.register(r'contract', corehr_api_views.ContractViewSet)
corehr_router.register(r'department', corehr_api_views.DepartmentViewSet)
corehr_router.register(r'absence', corehr_api_views.AbsenceViewSet)
corehr_router.register(r'absencetype', corehr_api_views.AbsenceTypeViewSet)

root = SimpleRouter

urlpatterns = [
path('admin/', admin.site.urls),
path('', include('corehr.urls', namespace='corehr')),
# path('api/', include('corehr_api.urls', namespace='corehr_api')),
path('api/corehr/', include(corehr_router.urls)),
# path('api/user/', include('users.urls', namespace='users')),
path('api/users/', include(users_router.urls)),
path('api-auth/', include('rest_framework.urls')),
path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
path('admin/doc/', include('django.contrib.admindocs.urls'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
    path('__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns