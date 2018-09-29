from rest_framework import serializers
from blog.models import Blog


class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = (
            'id',
            'title',
            'user',
            'img',
            'content',
            'created_at',
            'updated_at',
            'views_count',
            'is_starred',
        )
