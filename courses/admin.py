from django.contrib import admin
from .models import *
# Register your models here.


admin.site.register(Course)
admin.site.register(CourseReview)
admin.site.register(Instructor)
admin.site.register(Category)