from rest_framework import serializers
from .models import Blog, Tag, Image


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ('id', 'tag_name')


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ('id', 'title', 'url', 'top')


class BlogSerializer(serializers.ModelSerializer):
    tags = TagSerializer(many=True)
    images = ImageSerializer(many=True)

    class Meta:
        model = Blog
        fields = ('id', 'title', 'tags', 'content', 'update_time', 'images')
