from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)  # 생성된 토큰 가져오기

        # 사용자 지정 클레임 설정하기
        token['id'] = user.id
        token['username'] = user.username
        # ...
        return token