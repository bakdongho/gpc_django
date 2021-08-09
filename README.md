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

참고 사이트 : https://swarf00.github.io/

