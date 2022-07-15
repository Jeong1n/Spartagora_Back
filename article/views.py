from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status, permissions
from .serializers import ArticleSerializer, CommentSerializer
from .models import Article, Comment
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
        topic_best= Article.objects.all().order_by('-count')
        bestarticle_data = ArticleSerializer(topic_best, many=True).data
        return Response({"besttopic": bestarticle_data}, status=status.HTTP_200_OK)

class LowerAskView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    authentication_class = [JWTAuthentication]

    def get(self,request):
        return True


class LowerTravelEatView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    authenication_class = [JWTAuthentication]
    def get(self,request):
        return True
    def post(self,request):
        return True

class LowerHealthView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    def get(self,request):
        return True
