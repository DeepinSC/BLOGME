from rest_framework import viewsets
from blog.models import Blog
from blog.api.paginations import BlogPagination
from serializers import BlogSerializer


class BlogViewSet(viewsets.ModelViewSet):
    queryset = Blog.objects.all()
    pagination_class = BlogPagination
    serializer_class = BlogSerializer
