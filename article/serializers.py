from dataclasses import field
from rest_framework import serializers
from datetime import datetime
from django.utils import dateformat
from .models import Comment, UpperCategory, LowerCategory, Article

class UpperCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = UpperCategory
        fields = "__all__"


class LowerCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = LowerCategory
        fields = "__all__"


class CommentSerializer(serializers.ModelSerializer):
    username = serializers.SerializerMethodField(read_only=True)
    created_at = serializers.SerializerMethodField()

    def get_username(self, obj):
        return obj.user.username

    def get_created_at(self, obj):
        return dateformat.format(obj.created_at, 'y.m.d H시 i분')

    class Meta:
        model = Comment
        fields = "__all__"


class ArticleSerializer(serializers.ModelSerializer):
    category_set = LowerCategory()
    # image_path = serializers.SerializerMethodField(read_only=True)

    # def get_image_path(self, obj):
    #     return 'http://127.0.0.1:8000'+obj.image.url
    # username = serializers.SerializerMethodField(read_only=True)

    # def get_username(self, obj):
    #     return obj.user.username

    def create(self, validated_data):
        # User object 생성
        article = Article(**validated_data)
        article.save()
        return validated_data

    def update(self, instance, validated_data):
        today = datetime.today().strftime("%Y-%m-%d")
        for key, value in validated_data.items():
            if key == "Contents":
                value += f' {today}에 수정되었습니다.'
                continue
            setattr(instance, key, value)
        instance.save()
        return instance

    class Meta:
        model = Article
        fields = "__all__"