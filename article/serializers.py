from dataclasses import field
from re import T
from pytz import timezone
from rest_framework import serializers
from datetime import datetime, timedelta
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
        return dateformat.format(obj.created_at, 'y.m.d H:i')

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
    created_at = serializers.SerializerMethodField(read_only=True)
    assignment = serializers.SerializerMethodField(read_only=True)
    comment_count = serializers.SerializerMethodField(read_only=True)
    lower_category_name = serializers.SerializerMethodField(read_only=True)
    lower_category_url = serializers.SerializerMethodField(read_only=True)
    # 0000
    
    def get_lower_category_url(self,obj):
        return(obj.lower_category.lower_category_url)

    def get_lower_category_name(self, obj):
        return(obj.lower_category.lower_category)

    def get_assignment(self, obj):
        return(obj.user.assignment.assignment)

    def get_comment_count(self, obj):
        return(obj.comment_set.count())

    def get_created_at(self, obj):
        return dateformat.format(obj.created_at, 'y.m.d H:i')

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
        extra_kwargs= {
            "like" : {"read_only" : True}
        }
        model = Article
        fields = "__all__"