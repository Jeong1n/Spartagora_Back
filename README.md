# Spartagora_Back
최종프로젝트 스파르타고라 백엔드
## 프로젝트 주제 (스파르타고라)
* sparta + agora = spartagora
   * 스파르타코딩클럽 과정을 수강중 혹은 수료한 학생들의 익명 커뮤니티
   * 익명성이 보장된 상태에서 다양한 주제를 관해 이야기하는 커뮤니티
   <br><br>
   <div align="center">
   <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=Python&logoColor=white">
   <img src="https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=Django&logoColor=white">
   <img src="https://img.shields.io/badge/SQLite-003B57?style=for-the-badge&logo=SQLite&logoColor=white">
  </div>


## 맡은 역할
* 백앤드 Models, serializers, views 작성
* 게시글 보기
* 게시글 쓰기
* 게시글 수정, 삭제
* 프론트앤드와 연동(Javascript)

## Environment

* Django==4.0.6
* django-cors-headers==3.13.0
* djangorestframework==3.13.1
* djangorestframework-simplejwt==5.2.0
* jmespath==1.0.1
* PyJWT==2.4.0

## ERD
![image](https://user-images.githubusercontent.com/102134953/178625920-d3ef10a0-a71e-4b8f-a4c2-7daaf890eea1.png)

## API개발문서
![image](https://user-images.githubusercontent.com/102134953/178635347-82db6476-b1be-4758-a28d-7032ddab45e7.png)

## 트러블슈팅
1.글작성 폼에 관한 부분인데 summernote를 활용해서 글의 디자인을 풍성하게 하려했습니다.<br>
  하지만 데이터베이스의 저장, 수정에 관해 글이 잘 연계되지 않는 부분이 있었고 검색을 통해 공식문서를 참고해 문제를 해결했습니다.
  <br>
2.스파르타 수강생만 이용할 수 있도록 인증할 수 있는 시스템에 대해 논의했는데 스파르타 코딩클럽 회사소유의 개인정보에 대한 사인의 사용이 허락되지 않아<br>
  이부분에 대해서는 따로 인증을 거치지않고 회원가입 유저의 assignment 모델을 만들어 받기로 우회하였습니다.

## 팀원별 역할
| 팀원 | 이름 | 역할 | 깃허브 |
|:----------:|:----------:|:----------:|:----------:|
| **서크라테스** | 서정인 | 팀장 & 백엔드 |<a href="https://github.com/Jeong1n"><img src="https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=GitHub&logoColor=white"><a>|
| **안리스토텔리스** | 안정환 | 딥러닝 & 프론트엔드 |<a href="https://github.com/ajh1531"><img src="https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=GitHub&logoColor=white"><a>|
| **후라톤** | 김정후 | 백엔드 |<a href="https://github.com/fattysphinxx"><img src="https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=GitHub&logoColor=white"><a>|
| **혁피스트** | 김혁진 | 프론트엔드 |<a href="https://github.com/5aim"><img src="https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=GitHub&logoColor=white"><a>|
  
## 팀원간 약속
* 1 day 1 commit !!!!
* API Table, DB 구성을 아주 체계적이고 확실하게.
* 1시간 이상 디버깅이 지속될 경우 팀원과 소통 필수 또는 에러 공유하기
* 필수기능구현에 대한 역할분배의 비율을 나눠서 일정관리를 확실히하기
* 프로젝트 중엔 최대한 집중!!

## 프로젝트 진행하며 느낀점
DRF를 좀 더 이해하며 쓸수있게되었고 백앤드 모델과 시리얼라이저를 더 잘 쓸수 있게되었다 프로젝트를 진행하며 트러블슈팅이나 오류가 나는부분을 검색과 주변사람들에게 끊임없이 질문하며 사람들에게 서슴없이 먼저 물어보고 혼자 해결하는 능력도 키울수있게 되었다.

프론트앤드 GitHub
https://github.com/SCC-AI-3/Spartagora_Front
