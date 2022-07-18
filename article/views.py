from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status, permissions
from .serializers import ArticleSerializer, CommentSerializer
from .models import Article, Comment,LowerCategory
from rest_framework_simplejwt.authentication import JWTAuthentication
from user.serializers import UserSerializer
from user.models import User
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, TemplateView
# Create your views here.



class MainPageView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [JWTAuthentication]
    
    def get(self, request):
        article = Article.objects.order_by('-created_at')
        article_data = ArticleSerializer(article, many=True).data
        return Response({'article_data': article_data}, status=status.HTTP_200_OK)
    def post(self, request):
        print(request.data)
        request.data['user'] = request.user.id
        article_serializer = ArticleSerializer(data=request.data)
        if article_serializer.is_valid():
            # validator를 통과했을 경우 데이터 저장
            article_serializer.save()

            return Response({"message": "정상"}, status=status.HTTP_200_OK)

        return Response(article_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request, obj_id):
        print(request.user.id)
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
        print(obj_id)
        my_Article = Article.objects.get(id=obj_id)
        if request.user.id == my_Article.user.id:
            my_Article.delete()
            return Response({"message": "삭제 완료!"})
        return Response({"message":"권한이 없습니다"},status=status.HTTP_400_BAD_REQUEST)
class LowerTopicBestView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    def get(self,request):
        topic_best= Article.objects.all().order_by('-count')
        bestarticle_data = ArticleSerializer(topic_best, many=True).data
        return Response({"besttopic": bestarticle_data}, status=status.HTTP_200_OK)

class LowerCategoryView(APIView):
    # permission_classes = [permissions.IsAuthenticated]
    # authentication_class = [JWTAuthentication]

    def get(self,request,category_id):
        lower_category = LowerCategory.objects.get(id=category_id)  #카테고리 id값
        articles = Article.objects.filter(lower_category=lower_category) # 카테고리에 속해 있는 게시물 전부 불러오기
        serialized_data = ArticleSerializer(articles, many=True).data
        return Response(serialized_data, status=status.HTTP_200_OK)        


class Count(APIView):
    permission_classes = [permissions.IsAuthenticated]
    authentication_class = [JWTAuthentication]

    def update_counter(self):
        self.count = self.count + 1
        self.save()

class TaggedObjectLV(APIView):
    model = Article

    def get(self):
        taggit =  Article.objects.filter(tags__name=self.kwargs.get('tag'))
        return Response(taggit, status=status.HTTP_200_OK)  
    def get_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tagname'] = self.kwargs['tag']
        return Response(context, status=status.HTTP_200_OK)  

