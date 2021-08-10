# gpc_django

## 개요

장고로 간단한 웹사이트를 만드는 것을 공부하려 하는데, 간단하게 예제를 따라하면서 테크닉을 익히려고 한다!



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

