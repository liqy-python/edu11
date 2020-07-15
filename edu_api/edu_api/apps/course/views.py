from rest_framework.generics import ListAPIView, RetrieveAPIView

from rest_framework.filters import OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend

from course.models import CourseCategory, Course, CourseChapter
from course.pagination import CoursePageNumber
from course.serializer import CourseCategorySerializer, CourseModelSerializer, DetailModelSerializer, \
    CourseChapterModerSerializer


class CourseCategoryListAPIView(ListAPIView):
    """课程分类信息查询"""
    queryset = CourseCategory.objects.filter(is_show=True, is_delete=False).order_by("orders")
    serializer_class = CourseCategorySerializer


class CourseListAPIView(ListAPIView):
    """课程列表查询"""
    queryset = Course.objects.filter(is_show=True, is_delete=False).order_by("orders")
    serializer_class = CourseModelSerializer


class CourseFilterListAPIView(ListAPIView):
    """根据条件查询课程"""
    queryset = Course.objects.filter(is_show=True, is_delete=False).order_by("orders")
    serializer_class = CourseModelSerializer

    # 根据不同的分类id查询不同的课程
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filter_fields = ("course_category",)
    # 排序
    ordering_fields = ("id", "students", "price")
    # 分页   只能有一个
    pagination_class = CoursePageNumber


class DetailListAPIView(RetrieveAPIView):
    lookup_field = "id"
    queryset = Course.objects.filter(is_show=True, is_delete=False).order_by("orders", "-id")
    serializer_class = DetailModelSerializer


class CourseLessionListAPIView(ListAPIView):
    lookup_field = "id"
    queryset = CourseChapter.objects.filter(is_show=True, is_delete=False).order_by("orders", "id")
    serializer_class = CourseChapterModerSerializer
    filter_backends = [DjangoFilterBackend]
    filter_fields = ['course']
