
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
from django.conf.urls import include, url
from rest_framework_jwt.views import obtain_jwt_token
from rest_framework_jwt.views import refresh_jwt_token
from rest_framework_jwt.views import verify_jwt_token
from users.views import BlacklistTokenUpdateView

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
path('admin/doc/', include('django.contrib.admindocs.urls')),
path('admin/', admin.site.urls),
path('', include('corehr.urls', namespace='corehr')),
path('api/corehr/', include(corehr_router.urls)),
path('api/users/', include(users_router.urls)),
path('api-auth/', include('rest_framework.urls')),
path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
path('api/token/verify/', users_views.VerifyUser.as_view()),
path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),    
path('api/users/logout/blacklist/', BlacklistTokenUpdateView.as_view(),
         name='blacklist')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
    path('__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns