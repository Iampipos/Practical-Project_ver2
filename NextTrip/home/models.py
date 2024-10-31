from django.db import models

# Create your models here.

class UserProfile(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)
    gender = models.CharField(max_length=10, choices=[('female', 'ผู้หญิง'), ('male', 'ผู้ชาย'), ('other', 'อื่นๆ')])
    age_group = models.CharField(max_length=10, choices=[
        ('under18', 'ต่ำกว่า 18'),
        ('18-24', '18-24'),
        ('25-34', '25-34'),
        ('35-44', '35-44'),
        ('45-54', '45-54'),
        ('55-64', '55-64'),
        ('64+', '64 ขึ้นไป'),
    ])
    favorite_types = models.ManyToManyField('TourType', blank=True)  # เชื่อมกับประเภทการท่องเที่ยวที่ชื่นชอบ

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class TourType(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name
