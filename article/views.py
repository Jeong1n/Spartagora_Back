from sqlite3 import Timestamp
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status, permissions
from .serializers import ArticleSerializer, CommentSerializer
from .models import Article, Comment,LowerCategory, UpperCategory
from rest_framework_simplejwt.authentication import JWTAuthentication
from user.serializers import UserSerializer
from user.models import User
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, TemplateView
from copy import deepcopy
import boto3
from datetime import datetime

# Create your views here.



class MainPageView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [JWTAuthentication]
    
    def get(self, request):
        article = Article.objects.order_by('-created_at')
        article_data = ArticleSerializer(article, many=True).data
        return Response({'article_data': article_data}, status=status.HTTP_200_OK)
    def post(self, request):
        data = request.data.copy()
        data["user"] = request.user.id
        # pic = data["image"][0]
        # filename = datetime.now().strftime('%Y%m%d%H%M%S%f') + pic.name
        # s3 = boto3.client('s3') 
        # s3.put_object( 
        # ACL="public-read", 
        # Bucket="spartagora", 
        # Body=pic, 
        # Key=filename, 
        # ContentType=pic.content_type
        # )
        article_serializer = ArticleSerializer(data=data)
        if article_serializer.is_valid():
            # validator를 통과했을 경우 데이터 저장
            article_serializer.save()

            return Response({"message": "정상"}, status=status.HTTP_200_OK)

        return Response(article_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request, obj_id):
        
        article = Article.objects.get(id=obj_id)
        # user = User.objects.get(id=article.user.id)
        if request.user.id == article.user.id:
            article_serializer = ArticleSerializer(
                article, data=request.data, partial=True)
            if article_serializer.is_valid():
                # validator를 통과했을 경우 데이터 저장
                article_serializer.save()
                return Response({"message": "정상"}, status=status.HTTP_200_OK)
        return Response(article_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self,request, obj_id):
        my_Article = Article.objects.get(id=obj_id)
        if request.user.id == my_Article.user.id:
            my_Article.delete()
            return Response({"message": "삭제 완료!"})
        return Response({"message":"권한이 없습니다"},status=status.HTTP_400_BAD_REQUEST)



class LowerTopicBestView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    def get(self,request):
        get_lower_category = LowerCategory.objects.filter(upper_category = 1)
        topic_best = Article.objects.filter(lower_category__in=get_lower_category).order_by('-count')
        bestarticle_data = ArticleSerializer(topic_best, many=True).data
        return Response(bestarticle_data, status=status.HTTP_200_OK)

class LowerCategoryView(APIView):
    # permission_classes = [permissions.IsAuthenticated]
    # authentication_class = [JWTAuthentication]

    def get(self,request,category_id):
        lower_category = LowerCategory.objects.get(id=category_id)  #카테고리 id값
        articles = Article.objects.filter(lower_category=lower_category) # 카테고리에 속해 있는 게시물 전부 불러오기
        article = articles.order_by('-created_at')
        serialized_data = ArticleSerializer(article, many=True).data
        return Response(serialized_data, status=status.HTTP_200_OK)        


class Count(APIView):
    permission_classes = [permissions.IsAuthenticated]
    authentication_class = [JWTAuthentication]

    def get(self, request, obj_id):
        article = Article.objects.get(id=obj_id)
        article.count += 1
        article.save()
        return Response(status=status.HTTP_200_OK)

class TaggedObjectLV(APIView):
    model = Article

    def get(self):
        taggit =  Article.objects.filter(tags__name=self.kwargs.get('tag'))
        return Response(taggit, status=status.HTTP_200_OK)  
    def get_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tagname'] = self.kwargs['tag']
        return Response(context, status=status.HTTP_200_OK)  

class CommentView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    def get(self,request,obj_id):
        get_article = Article.objects.get(id = obj_id)
        get_comment = Comment.objects.filter(article = get_article)
        serialized_data = CommentSerializer(get_comment, many=True).data
        return Response(serialized_data, status=status.HTTP_200_OK)
    
    def post(self,request,obj_id):
        request.data["user"] = request.user.id
        request.data["article"] = obj_id
        request.data["content"] = request.data["comment"]
        serialized_comment = CommentSerializer(
            data=request.data)
        if serialized_comment.is_valid():
            serialized_comment.save()
            return Response(serialized_comment.data, status=status.HTTP_200_OK)
        return Response(serialized_comment.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self,request,obj_id): #여기서의 obj_id는 댓글 
        comment_get = Comment.objects.get(id=obj_id)
        serialized_comment = CommentSerializer(comment_get, data=request.data, partial=True)
        # if request.user.id == comment_get.user.id:
        if serialized_comment.is_valid():
            serialized_comment.save()
            return Response(serialized_comment.data, status=status.HTTP_200_OK)
        return Response(serialized_comment.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request,obj_id): #여기서의 obj_id도 댓글
        comment_get = Comment.objects.get(id=obj_id)
        if request.user.id == comment_get.user.id:
            comment_get.delete()
            return Response({"message":"댓글이 삭제되었습니다."}, status=status.HTTP_200_OK)
        return Response({"message":"삭제할 권한이 없습니다"}, status=status.HTTP_400_BAD_REQUEST)

class DetailView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    def get(self,request,obj_id):
        article_get = Article.objects.get(id=obj_id)
        serialized_data = ArticleSerializer(article_get).data
        serialized_data['boolean'] = request.user in article_get.like.all()
        return Response(serialized_data,status=status.HTTP_200_OK)

class LikeView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [JWTAuthentication]
    
    
    def get(self,request,obj_id):
        article_get = Article.objects.get(id=obj_id)
        if request.user in article_get.like.all():
            for i in article_get.like.all():
                if request.user == i:
                    article_get.like.remove(i)
                    serialized_data = ArticleSerializer(article_get,data=request.data)
                    if serialized_data.is_valid():
                        serialized_data.save()
                else: continue
            return Response({"message":"좋아요 취소"}, status=status.HTTP_200_OK)
        else:    
            article_get.like.add(request.user.id)
            serialized_data = ArticleSerializer(article_get,data=request.data)
            if serialized_data.is_valid():
                serialized_data.save()
            return Response({"message":"좋아요 완료"}, status=status.HTTP_200_OK)
            