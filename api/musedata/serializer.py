from rest_framework import serializers
from .models import *

class CategorySerializers(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = "__all__"

class PostSerializer(serializers.ModelSerializer):
    categories = CategorySerializers(many=True)
    tags = TagSerializer(many=True)

    class Meta:
        model = Post
        fields = "__all__"
    
    def create(self, validated_data):
        categories_data = validated_data.pop('categories')
        tags_data = validated_data.pop('tags')
        post = Post.objects.create(**validated_data)
        
        post.categories.set([Category.objects.create(**category_data) for category_data in categories_data])
        post.tags.set([Tag.objects.create(**tag_data)for tag_data in tags_data])
        
        return post

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = "__all__"