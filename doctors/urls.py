from django.urls import path
from .views import *
urlpatterns = [
    path('reviews/', ReviewModelViewSet.as_view({
        'get': 'list', 'post': 'create'
        })),
    path('destinationname/', DestinationnamesModelViewSet.as_view({
        'get': 'list'
        })),
    path('destinationname/create', DestinationnamesCreateModelViewSet.as_view({
        'get': 'list', 'post': 'create'
        })),
    path('services/', ServicesModelViewSet.as_view({
        'get': 'list'
        })),
    path('services/create', ServicesCreateModelViewSet.as_view({
        'get': 'list', 'post': 'create'
        })),
    path('service/', ServiceModelViewSet.as_view({
        'get': 'list'
        })),
    path('service/create', ServiceCreateModelViewSet.as_view({
        'get': 'list', 'post': 'create'
        })),
    path('money/', MoneyModelViewSet.as_view({
        'get': 'list'
        })),
    path('money/create', MoneyCreateModelViewSet.as_view({
        'get': 'list', 'post': 'create'
        })),
    path('post/', PostModelViewSet.as_view({
        'get': 'list'
        })),
    path('post/create', PostCreateModelViewSet.as_view({
        'get': 'list', 'post': 'create'
        })),
    path('appointment/', AppointmentModelViewSet.as_view({
        'post': 'create'
        })),
    path('doctors/<int:id>/', DoctorDetailModelViewSet.as_view({
        "get": 'retrieve'
    })),
    path('doctors/', DoctorsModelViewSet.as_view({
        "get": 'list'
    })),
    path('doctors/create/', DoctorCreateModelViewSet.as_view({
        "post": 'create'
    })),
    # path('doctor/', DoctorDetailAPIView.as_view()),
    path('reviews/<int:id>/', ReviewModelViewSet.as_view({
        'get': 'retrieve', 'put': 'update', 'delete': 'destroy'
            })),
    path('records/<int:id>/', AppointmentModelViewSet.as_view({
        'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}))]