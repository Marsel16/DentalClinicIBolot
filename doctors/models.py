from django.db import models
from users.models import User
from phonenumber_field.modelfields import PhoneNumberField


# Create your models here.
from DentalClinicIBolot import settings


class Post(models.Model):
    post = models.CharField(max_length=50, verbose_name='Должность')
    class Meta:
        verbose_name = 'Должность'
        verbose_name_plural = 'Должности'

    def __str__(self):
        return self.post
class Doctor(models.Model):
    image = models.ImageField(default='user.jpg')
    name = models.CharField(max_length=255, verbose_name='Имя')
    last_name = models.CharField(max_length=255, verbose_name='Фамилия')
    datetime = models.DateField(verbose_name='Дата рождения')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, verbose_name='Должность')
    education = models.TextField(null=True, verbose_name='Образование')
    experience = models.IntegerField(verbose_name='Стаж работы')

    class Meta:
        verbose_name = "Информация о докторе"
        verbose_name_plural = "Добавить доктора"

    def __str__(self):
        return self.name

class Money(models.Model):
    money = models.PositiveIntegerField(verbose_name='Стоимость')
    class Meta:
        verbose_name = 'Стоимость'
        verbose_name_plural = 'Стоимости'
class Services(models.Model):
    image = models.ImageField()
    names = models.CharField(max_length=50, null=True, verbose_name='Услуга')

    class Meta:
        verbose_name = "Услуги"
        verbose_name_plural = "Услуги"

    def __str__(self):
        return self.names

class Destinationnames(models.Model):
    imag = models.ImageField()
    services = models.ForeignKey(Services, on_delete=models.CASCADE, verbose_name='Услуга')
    name = models.CharField(max_length=50, verbose_name='Названия направлений')

    class Meta:
        verbose_name = 'Названия направления'
        verbose_name_plural = 'Названия направлений'
    def __str__(self):
        return self.name
class Service(models.Model):
    image = models.ImageField()
    destination = models.ForeignKey(Destinationnames, on_delete=models.CASCADE, verbose_name='Названия направления')
    description = models.CharField(max_length=255, verbose_name='Описание праблемы')
    money = models.ForeignKey(Money, on_delete=models.CASCADE, verbose_name='Цены')
    doctor = models.ManyToManyField(Doctor, verbose_name='Доктора которых можно записаться')

    class Meta:
        verbose_name = 'Услуга'
        verbose_name_plural = 'Услуги'

class Appointment(models.Model):
    Time = (
        ('8', '08:00-09:20'),
        ('9', '09:30-10:50'),
        ('14', '14:00-15:20'),
        ('15', '15:30-16:50'),
        ('17', '17:00-18:20'),
        ('18', '18:30-20:00'),
    )
    first_name = models.CharField(max_length=100, verbose_name='Имя')
    last_name = models.CharField(max_length=100, verbose_name='Фамилия')
    phone_number = PhoneNumberField(max_length=13, default='+996', verbose_name="Номер телефона")
    date = models.DateField(verbose_name="Назначить Дату")
    time = models.CharField(max_length=2, choices=Time, verbose_name='Выбрать Время')
    service = models.ForeignKey(Service, on_delete=models.CASCADE, verbose_name="Выбрать Услугу", null=True)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, verbose_name="Выбрать Врача")

    class Meta:
        verbose_name = "Запись на Прием"
        verbose_name_plural = "Запись на прием"

    def __str__(self):
        return self.first_name
class Review(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True, verbose_name="Автор")
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, null=True, verbose_name="Выберите доктора",
                               related_name='doctor_reviews')
    text = models.TextField(max_length=255, verbose_name="Tекст")
    created_date = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name = "Отзыв"
        verbose_name_plural = "Отзывы"

