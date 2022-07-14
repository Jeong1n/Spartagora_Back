from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status, permissions
from .serializers import ArticleSerializer, CommentSerializer
from .models import Article, Comment,LowerCategory
from rest_framework_simplejwt.authentication import JWTAuthentication
from user.serializers import UserSerializer
from user.models import User
# Create your views here.

class ArticlePostView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    def post(self,request):
        request.data['user'] = request.user.id
        article_serializer = ArticleSerializer(data=request.data)
        if article_serializer.is_valid():
            article_serializer.save()

            return Response({"message": '작성완료'}, status=status.HTTP_200_OK)



class MainPageView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    def get(self,request):
        return True

class LowerTopicBestView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    def get(self,request):
        return True

class LowerCategoryView(APIView):
    # permission_classes = [permissions.IsAuthenticated]
    # authentication_class = [JWTAuthentication]

    def get(self,request,id):
        lower_category = LowerCategory.objects.filter(id=id)  #카테고리 id값
        articles = Article.objects.filter(lower_category=lower_category) # 카테고리에 속해 있는 게시물 전부 불러오기
        serialized_data = ArticleSerializer(articles, many=True).data
        return Response(serialized_data, status=status.HTTP_200_OK)        




