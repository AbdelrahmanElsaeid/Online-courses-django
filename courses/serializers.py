from rest_framework import serializers
from .models import Course,Category,CourseReview,Instructor






class CoursesReviewSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()
    class Meta:
        model = CourseReview
        fields = ['id','user', 'review', 'rate','data']

class CategoryListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'                

class InstructorListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Instructor
        fields = '__all__'         

class CoursesListSerializer(serializers.ModelSerializer):
    category = serializers.StringRelatedField()
    #instructor = serializers.StringRelatedField()
    class Meta:
        model = Course
        fields = '__all__'        

class CoursesDetailSerializer(serializers.ModelSerializer):
    category = serializers.StringRelatedField()
    instructor = serializers.StringRelatedField()
    review = CoursesReviewSerializer(source='course_review', many=True)

    class Meta:
        model = Course
        fields = '__all__'  