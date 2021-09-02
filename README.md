# BB(Bang for the Buck) Project

## 목차

1. [Introduction](#1-introduction)
2. [Don't forget!](#2-dont-forget) 
3. [Approach](#3-approach)
4. [Discovered Problem](#4-discovered-problem)
5. [To do list](#5-to-do-list)  


➕ [내가 알게 된것](#내가-알게된-것)

<br>

### 1. Introduction
- - -
지방에서 올라온 촌놈이 혼자 서울살이 하다보니 혼밥 또는 혼카페를 하는 경우가 대부분이다. 돈 없는 인원들의 생존을 위해 __식비와 커피로 나가는 돈을 아끼고 싶다.__ 맛집, 인기있는 이런 곳만 추천해주는 곳만 많지 __가성비가 좋은 밥집과, 카페를 알 수 있으면 얼마나 좋을까?__ 그래서 태어나게 되었다.  
__BB(Bang for the Buck - 가성비). 프로젝트.__ 😎 

<br>

### 2. Don't forget!
- - -
1. 이런 토이프로젝트의 본질은 내가 필요한 것을 재미있게 만드는 것이다. 내가 재미를 느끼고, 끝까지 만들어 보는 것에 의의를 두자
2. 거대 아키텍처를 구성하느라 시간 쏟지말자. 내가 이것을 배포한다 한들 서버가 터질 일은 하늘이 두 쪽 나도 없을 것이다.
3. 내가 사용해보지 않은 기술을 1~2가지 정도만 깔짝 대보자. 내가 익숙하지 않은 것으로 하다가 시작도 못한다.(공부할 게 많음)

<br>

### 3. Approach
- - -
아이디어는 간단하다. 🤩
1. 네이버 지도 API를 이용해 검색한 곳의 위치를 찾고
2. 그 위치를 주변의 밥집이나 카페의 데이터들을 네이버 지도 / 요기요에서 거리순으로 긁어와서
3. 가성비 공식으로 점수를 매긴다.
4. 점수가 높은 순서대로 보여준다.
5. 이후에 추가 기능들을 차차 업데이트할 예정

<br>

### 4. Discovered Problem
- - -
|number|Problem|Solution|
|---|---|---|
|1|웹에서 https 또는 local만 현재 위치 기능 사용 가능한 문제.|X|
|2|네이버와 요기요에서 점포가 겹치는 문제|X|
|3|요기요에서 배달전문인 점포 구별|X|

<br>

### 5. To do list
- - -
|number|To do|status|
|---|---|---|
|1|가성비 공식 만들어서 계산하기|
|2|화면 구성 설계, 다른 기능 구상|
|3|문장간 유사도 알고리즘을 통해 네이버 요기요 중 중복 점포 걸러보자|
|4|api에서 들고온 데이터를 참고해서 배달전문 점포 구분하기|

<br>
<br>

## 내가 알게된 것

### 1. View

1. CBV(Class Based View) : view를 개발할 때, 함수기반으로 짤 수도 있지만 생산성을 위해 주로 class로 개발 한다.  
   1. 제네릭 뷰 종류 : TemplateView, ListView, DetailView, CreateView, UpdateView 대표적  
      - template_name 으로 html 파일 path 설정해주고, def get 또는 def post 등으로 http method 처리를 할 수 있다. render_to_response 함수를 통해 template_name 등록된 template을 자동적으로 기본 템플릿 엔진을 통해 html로 변환해준다.  
      - urls.py 에서 .as_view()로 해당 view를 호출할 수 있다.
   2. 다른 제네릭뷰에서는 SingleObjectMixin, MultipleObjectMixin 등을 상속받아 정의가 되어 있다. 두 믹스인의 클래스변수를 미리 알아두면 좋을 것 같으니 메소드는 소스코드를 참고해서 공부해보자


### 2. template

1. template 상속과 블록
   - html에 상단에 {% extends 'base.html' %} 한 줄 추가하여 base.html의 구조를 그대로 사용할 수 있다.
   - {% block css %} <link scr="#"> {% endblock css %} 과 같이 블록된 부분은 오버라이드할 수 있다.
   - 부모템플릿의 내용을 인용시 {{ block.super }} 변수 사용 가능

2. template 필터

   - 줄바꿈('\n')이 html에서 적용이 안됨. 필터라는 것을 사용해 다른 함수를 사용할 수 있다. 파이프('|')로 연결하여 적용할 함수 적으면 됨.  
ex) 줄바꿈 html \<br>로 변경 => {{ article.content | linebreaksbr }} / 날짜 포매팅 => {{ article.created_at | date:"Y-m-d H:i" }}

3. messages
   - 메세지 내용을 기록하면 템플릿에서 데이터를 출력할 때까지 임시로 데이터를 저장해두는 프레임워크. 로그처럼 레벨(debug, info, success, warning, error)이 있기에, 오류나 단순 정보와 같은 것을 구분하기 좋음. 
   - views.py에서 요청을 처리하는 로직 중에 일어나는 상태들을 메세지로 담아서 보낼 수 있다. ex) post 요청시 키 값이 없을때, "값이 존재하지 않습니다." error 레벨로 저장하여 보여주기.
   - views.py에서 context로 전달하지 않아도 장고에서 템플릿으로 messages라는 객체로 저장된 메시지들이 전달된다.

### 3. 사용자인증

시작하기에 앞서, django는 auth 프레임워크처럼 이미 구현된 기본 기능들이 되게 많다. 하지만 현실은 몰라서 못쓰고 있지 않는가? 그렇기 때문에, __각 기능들이 어떻게 구현되어 있는지를 코드를 까서 보면서 이해하는 것이 중요하다.__ 왜냐하면 제일 큰 이유는 이것을 이해해야 내가 적절한 상황에서 가져다 쓸 수 있어야하기 때문이고, 불가피하게 수정해야 하는 부분이 생기면 커스텀을 할 수 있다는 것이다.

   1. User model custom : AbstractBaseUser, PermissionsMixin를 상속 받아서 각 필드들을 작성해주면된다. Meta class의 abstract = True가 되면 makemigrations 커맨드에 실행 무시하는 옵션.
   2. Meta class는 outer 클래스의 옵션을 설정한다. ordering(정렬), indexes(인덱스부여), unique_together(다중필드 유니크), index_together 등이 있다.



참고 사이트 : https://swarf00.github.io/

<br>

## 시간을 많이 잡아먹은 ERROR

### 1. NoReverseMatch ERROR

- reference : https://stackoverflow.com/questions/38390177/what-is-a-noreversematch-error-and-how-do-i-fix-it
> The NoReverseMatch exception is raised by django.core.urlresolvers when a matching URL in your URLconf cannot be identified based on the parameters supplied.

이 에러가 발생하는 원인에 대해서 위과 같이 설명한다. 즉 url,파라미터를 제대로 제공하지 못해 매칭되는 것을 url을 django가 찾지 못하는 것이다. url을 정의 해주는 부분만 찾아보면 쉽게 해결할 수 있는 에러이다. 그렇게 어려운 에러가 아니지만 내가 왜 헤매었는지, 생각해보면 '여긴 슥 봤는데, 잘 되어 있어, 틀린 것이 절대 없을 거야' 라고 안일하게 생각하던 버릇때문에 꼬박 하루 넘게를 날렸다. 

원인은 template html 파일에 `{% url 'myapp:update' %}` 이 부분이었다. 이곳이 가르키는 url은 (`/<article_id>/update`) 파라미터가 필요한 url인데 파라미터를 전달해주지 못했기 때문에 일어난 에러였다. 그래서 단순히 `{% url 'myapp:update' article.pk %}` article.pk 만 같이 보내주는 되는거였다. 

절대 안보려던 html 파일에서 이걸 찾게된 이유는, 다른 페이지를 만들어서 실험을 하는데 잘되는데 저 페이지만 안되는 것이었다. 그래서 작동하는 원리를 따라다가보니, 장고가 해당 url과 연결된 함수를 실행시키면서, template에서 html 파일을 찾아 쭉 읽어서 jinja 문법을 파싱하여 값을 다 바꿔서 rendering 하는 식이었다. 그 과정중에 난 분명 파라미터를 명시하여 넘겨준다고 생각했는데, 없으니 이상하다 생각하고 자세히 본 결과 빼먹었다는 것을 알게되었고 수정하면서 쉽게 해결했다. 

진짜 컴퓨터는 에러 메세지를 던지면서 안되는 이유를 잘 알려준다. "왜 맞는데 틀리지?" 라는 생각은 정말 어리석은 것 같다. 항상 의심하고, 에러가 나는 원인을 정확히 알고 그 부분을 중점적으로 디버깅 할 수 있도록 노력하자. 그랬다면 금방 찾아서 해결됐을 것이다.

