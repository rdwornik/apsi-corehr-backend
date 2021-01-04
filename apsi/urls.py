
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from rest_framework.routers import DefaultRouter
from users import views

router = DefaultRouter(trailing_slash=False)
router.register(r'employees', views.EmployeeViewSet)

urlpatterns = [
path('admin/', admin.site.urls),
path('', include('corehr.urls', namespace='corehr')),
path('api/', include('corehr_api.urls', namespace='corehr_api')),
# path('api/user/', include('users.urls', namespace='users')),
path('api/user/', include(router.urls)),
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