import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')
import django
django.setup()
from faker import Faker
import random
from courses.models import Course, Category,Instructor,CourseReview
from django.contrib.auth.models import User
from django.utils import timezone



def seed_category(n):
    fake = Faker()
    for x in range(n):
        Category.objects.create(
            name = fake.name(),
        )
    print(f"{n} category Seed ")

def seed_instructor(n):
    fake = Faker()
    images = ['1.jpg', '2.jpg', '3.jpg', '4.jpg', '5.jpg', '6.jpg', '7.jpg', '8.jpg', '9.jpg', '10.jpg' ]
    for x in range(n):
        Instructor.objects.create(
            name = fake.name(),
            subtitle = fake.text(max_nb_chars = 100),
            about = fake.text(max_nb_chars = 300),
            image = f"instructor/{images[random.randint(0,9)]}",
            ln_link = 'http://127.0.0.1:8000/',
            tw_link = 'http://127.0.0.1:8000/',
        )
    print(f"{n} category Seed ")



def seed_course(n):
    fake = Faker()
    for x in range(n):
        Course.objects.create(
            name = fake.name(),
            price  = round(random.uniform(20.99, 99.99),2),
            short_description = fake.text(max_nb_chars = 300),
            description = fake.text(max_nb_chars = 4000),
            category = Category.objects.get(id = random.randint(1,9)),
            instructor = Instructor.objects.get(id = random.randint(1,9)),

        )
    print(f"{n} course Seed ")

def seed_course_review(n):
    fake = Faker()
    for x in range(n):
        CourseReview.objects.create(
            user=User.objects.get(id=1),
            course=Course.objects.get(id = random.randint(1,800)),
            review = fake.text(max_nb_chars = 300),
            rate= random.randint(1,6),
            data = timezone.now() - timezone.timedelta(days=7),
            

        )
    print(f"{n} CourseReview Seed ")


#seed_category(10)
#seed_instructor(10)
#seed_course(800)
#seed_course_review(500)
