from django.contrib import admin
from django.urls import path, include
from .api import course_list, CourseList,CourseDetail,CategoryList

app_name='courses'

urlpatterns = [
    #path('courses/', course_list),
    path('courses/',CourseList.as_view()),
    path('courses/<int:pk>/',CourseDetail.as_view()),
    path('category/', CategoryList.as_view())

]