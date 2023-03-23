from rest_framework.pagination import PageNumberPagination
from rest_framework.viewsets import ModelViewSet
from .models import Review, Doctor, Appointment, Service, Services, Destinationnames, Post, Money
from .serializers import *

from rest_framework.permissions import IsAdminUser, IsAuthenticated

# Create your views here.


class ReviewModelViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    pagination_class = PageNumberPagination
    lookup_field = 'id'

class AppointmentModelViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer
    pagination_class = PageNumberPagination
    lookup_field = 'id'

class PostModelViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    pagination_class = PageNumberPagination
    lookup_field = 'id'
class PostCreateModelViewSet(ModelViewSet):
    permission_classes = [IsAdminUser]
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    pagination_class = PageNumberPagination
    lookup_field = 'id'

class ServicesModelViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Services.objects.all()
    serializer_class = ServicesSerializer
    pagination_class = PageNumberPagination
    lookup_field = 'id'

class ServicesCreateModelViewSet(ModelViewSet):
    permission_classes = [IsAdminUser]
    queryset = Services.objects.all()
    serializer_class = ServicesSerializer
    pagination_class = PageNumberPagination
    lookup_field = 'id'

class ServiceModelViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer
    pagination_class = PageNumberPagination
    lookup_field = 'id'

class ServiceCreateModelViewSet(ModelViewSet):
    permission_classes = [IsAdminUser]
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer
    pagination_class = PageNumberPagination
    lookup_field = 'id'

class DestinationnamesModelViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Destinationnames.objects.all()
    serializer_class = DestinationnamesSerializer
    pagination_class = PageNumberPagination
    lookup_field = 'id'

class DestinationnamesCreateModelViewSet(ModelViewSet):
    permission_classes = [IsAdminUser]
    queryset = Destinationnames.objects.all()
    serializer_class = DestinationnamesSerializer
    pagination_class = PageNumberPagination
    lookup_field = 'id'

class MoneyModelViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Money.objects.all()
    serializer_class = MoneySerializer
    pagination_class = PageNumberPagination
    lookup_field = 'id'

class MoneyCreateModelViewSet(ModelViewSet):
    permission_classes = [IsAdminUser]
    queryset = Money.objects.all()
    serializer_class = MoneySerializer
    pagination_class = PageNumberPagination
    lookup_field = 'id'

class DoctorsModelViewSet(ModelViewSet):
    queryset = Doctor.objects.all()
    serializer_class = DoctorsSerializer
    pagination_class = PageNumberPagination
    lookup_field = 'id'

class DoctorDetailModelViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Doctor.objects.all()
    serializer_class = DoctorDetailSerializer
    pagination_class = PageNumberPagination
    lookup_field = 'id'

class DoctorCreateModelViewSet(ModelViewSet):
    permission_classes = [IsAdminUser, IsAuthenticated]
    queryset = Doctor.objects.all()
    serializer_class = DoctorsSerializer
    pagination_class = PageNumberPagination
    lookup_field = 'id'


