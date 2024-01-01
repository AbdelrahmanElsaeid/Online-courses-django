from django.utils import timezone
from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=30)
    def __str__(self):
        return self.name

class Course(models.Model):
    name = models.CharField(max_length=50)
    short_description = models.TextField(max_length=100)
    description = models.TextField(max_length=300)
    price = models.FloatField()
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, related_name='course_category')
    instructor = models.ForeignKey('Instructor', on_delete=models.CASCADE, related_name="instructors_course")


    def __str__(self):
        return self.name
    
    def avg_rate(self):
        reviews = self.course_review.all()
        if (reviews)>0:
            re_sum=0
            for i in reviews:
                re_sum+=i.rate
            return round(re_sum/len(reviews),1)
        else:
            return 0

class CourseReview(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='course_review')
    review = models.TextField(max_length=200)
    rate = models.IntegerField()
    data = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return str(self.user)
    
        

class Instructor(models.Model):
    name = models.CharField(max_length=150)
    subtitle = models.CharField(max_length=300)
    image = models.ImageField(upload_to='instructors')
    about = models.TextField(max_length=200)
    ln_link = models.URLField(null=True, blank=True)
    tw_link = models.URLField(null=True, blank=True)

    def __str__(self):
        return self.name    