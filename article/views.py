from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status, permissions
from .serializers import ArticleSerializer, CommentSerializer
from .models import Article, Comment,LowerCategory
from rest_framework_simplejwt.authentication import JWTAuthentication
from user.serializers import UserSerializer
from user.models import User
from django.contrib.auth.decorators import login_required
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
    
    def get(self, request):
        Article = Article.objects.order_by('-created_at')
        Article_data = ArticleSerializer(Article, many=True).data
        return Response({'Article_data': Article_data}, status=status.HTTP_200_OK)
    def post(self, request):
        print(request.data)
        request.data['user'] = request.user.id
        Article_serializer = ArticleSerializer(data=request.data)
        if Article_serializer.is_valid():
            # validator를 통과했을 경우 데이터 저장
            Article_serializer.save()

            return Response({"message": "정상"}, status=status.HTTP_200_OK)

        return Response(Article_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, obj_id):
        Article = Article.objects.get(id=obj_id)

        # 기본적인 사용 방법은 validator, creater와 다르지 않다.
        # update를 해줄 경우 obj, data(수정할 dict)를 입력한다.
        # partial=True로 설정해 주면 일부 필드만 입력해도 에러가 발생하지 않는다.
        Article_serializer = ArticleSerializer(
            Article, data=request.data, partial=True)
        if Article_serializer.is_valid():
            # validator를 통과했을 경우 데이터 저장
            Article_serializer.save()
            return Response({"message": "정상"}, status=status.HTTP_200_OK)
        return Response(Article_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    @login_required()
    def delete(request, obj_id):
        my_Article = Article.objects.get(id=obj_id)
        my_Article.delete()
        return Response({"message": "로그아웃 성공!"})

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

class count(APIView):
    permission_classes = [permissions.IsAuthenticated]
    authentication_class = [JWTAuthentication]

    def update_counter(self):
        self.count = self.count + 1
        self.save()

