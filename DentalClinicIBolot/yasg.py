from django.urls import path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

scheme_view = get_schema_view(
    openapi.Info(
        title='DentalClinic',
        default_version='v1',
        description='Test DentalClinic',
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@snippets.local"),
        license=openapi.License(name="BSD license"),

    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    path('swagger(?P<format>\.json|\.yaml)$', scheme_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', scheme_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', scheme_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]

