from rest_framework import serializers
from .models import Review, Doctor, Appointment, Money, Services, Service, Destinationnames, Post
from users.serializers import UserSerializer
from users.models import User

class ReviewSerializer(serializers.ModelSerializer):
    # author_name = serializers.SerializerMethodField()
    class Meta:
        model = Review
        fields = 'id text author doctor created_date'.split()
    # def get_author_name(self, obj):
        # user = User.objects.get(id=obj.a)
        # return user.first_name

class DoctorReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = 'id text author  created_date'.split()

class DoctorsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = '__all__'

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'

class ServicesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Services
        fields = '__all__'

class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = '__all__'

class DestinationnamesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Destinationnames
        fields = '__all__'
class MoneySerializer(serializers.ModelSerializer):
    class Meta:
        model = Money
        fields = '__all__'

class DoctorDetailSerializer(serializers.ModelSerializer):
    doctor_reviews = DoctorReviewSerializer(many=True)
    class Meta:
        model = Doctor
        fields = 'id image name last_name datetime post education experience doctor_reviews'.split()

    def get_review(self, doctor):
        return [i.text for i in doctor.review.all()]

class AppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appointment
        fields = 'id phone_number date service doctor'.split()

