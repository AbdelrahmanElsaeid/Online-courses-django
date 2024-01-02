from .models import Course, Category
from .serializers import CoursesListSerializer, CoursesDetailSerializer,CategoryListSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import generics
import django_filters.rest_framework
from rest_framework import filters

@api_view(['GET'])
def course_list(request):
    query = Course.objects.all()
    data = CoursesListSerializer(query, many=True).data
    return Response({'data': data})

class CourseList(generics.ListCreateAPIView):
    queryset=Course.objects.all()
    serializer_class = CoursesListSerializer
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend,filters.SearchFilter,filters.OrderingFilter]
    filterset_fields = ['category', 'name']
    search_fields = ['name']
    ordering_fields = ['price']

class CourseDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset=Course.objects.all()
    serializer_class = CoursesDetailSerializer   


class CategoryList(generics.ListCreateAPIView):
    queryset=Category.objects.all()
    serializer_class = CategoryListSerializer
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filterset_fields = [ 'name']    