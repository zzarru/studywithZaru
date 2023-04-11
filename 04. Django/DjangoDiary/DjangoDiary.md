# Django Diary

###### Django 뿌신다.

작성자 : zaru



[Django 공식문서 바로가기](https://docs.djangoproject.com/en/4.1/)



### 기본 설정

**가상환경 세팅하기**

`python -m venv [가상환경 이름]` : 가상환경 설치하기. 

이 때, 가상환경 이름은 똑같이 'venv'로 지정하여 사용한다. (권장사항)

> `-m`  : 모듈을 탐색하거나 실행하거나 한다. 

`source venv/Scripts/activate` (winOS) / `source venv/bin/activate` (MacOS) : 가상환경 실행하기

-- 가상화면 실행 결과 확인하기 : (venv)가 떠있으면 가상환경 실행된 거임 --

<img src=".\01. venv.png"  />

`deactivate` : 가상환경 비활성화



**pip 설치하기**치

###### ! pip란 파이썬으로 작성된 패키지 소프트웨어를 설치 및 관리하는 시스템이다. 

`pip list` : 설치된 pip 목록을 볼 수 있다. 

`pip django==3.2.18` : 버전을 명시하지 않으면 가장 최신 버전이 설치된다. 

`pip freeze > requirements.txt` : 가상환경 패키지 목록 저장 

`pip install -r requirements.txt` : 가상환경 패키지 설치



**Django 프로젝트 만들기** ([프로젝트 시작하기 (공식문서 예제)](https://docs.djangoproject.com/en/4.1/intro/tutorial01/))

`django-admin startproject [프로젝트 이름] .` 

*프로젝트 이름 뒤에 .을 찍으면 알아서 풀리고 .을 안찍으면 project 폴더 안에 새로운 project 폴더를 생성한다. (폴더 안에 풀기) ; 이름이 낭비되기 때문에 기본적으로 .을 찍고 프로젝트를 만든다. 

<img src=".\02. django pjt.png" />

 프로젝트를 생성하면 manage.py가 자동으로 만들어진다. 

> `manage.py` : django 프로젝트와 소통하는 유틸리티
>
> 사용법 : `python manage.py <command> [options]` 





서버 실행하기 : `python manage.py runserver`

<img src=".\03. runserver.png">



(1)  `ctrl + 서버주소 클릭` 하면 서버 페이지 확인 가능하다. 

(2) runserver 하고 나면 자동으로 `db.sqlite3` 이 생성된다. 



-> 프로젝트 생성하고 나면 생기는 파일이랑 그 역할 정리하기





**Django 애플리케이션(앱) 생성하기**

`python manage.py startapp [앱 이름(복수형)]` : 일반적으로 앱 이름은  **복수형**으로 작성(권장)

> `django-admin startapp [앱 이름]` 으로도 앱을 생성할 수 있지만 권장하는 방식은 아니다. 

*앱(App) : 하나의 큰 기능 단위

**정해진 규칙은 없으며 개발자가 판단하여 앱을 생성한다. 



 **어플리케이션 등록하기**

앱을 사용하기 위해서 프로젝트의  `settings.py` 에서 INSTALLED_APPS 리스트에 반드시 추가해야한다. 

<img src=".\04. installed apps.png">

! 주의 'articles' 뒤에 , 빼먹지 않기! 



>프로젝트 vs 어플리케이션
>
>settings.py의 유무로 프로젝트와 어플리케이션을 구분한다. 어플리케이션의 경우에는 settings.py가 없다. 



> Projects vs. apps
>
> What’s the difference between a project and an app? An app is a web application that does something – e.g., a blog system, a database of public records or a small poll app. A project is a collection of configuration and apps for a particular website. A project can contain multiple apps. An app can be in multiple projects.
>
> 출처: [공식문서](https://docs.djangoproject.com/en/4.1/intro/tutorial01/)



-> 프로젝트랑 어플리케이션 역할 차이 더 공부해보기

앱 만들면 생성되는 파일에 대해서 공부하기!



### Django 흐름 이해하기

> urls - views - templates으로 흘러가는 구조를 이해한다.
>
> 1) home/ 으로 접속하면
> 2) views의 hola 함수가 실행되고
> 3) index.html을 통하여 "hola!"가 서버 화면에 뜨도록 한다.



1) urls.py

   <img src=".\07. urls.png" style="zoom:80%;" >
   
   `path('[urls/ 경로 입력]',views.index, name= 'index')`





2. views.py

   <img src=".\08. views.png"  >



3. index.html

   <img src=".\09. index.png" style="zoom: 50%;" >

### Template

**Templates 생성하기**

: 실제 화면에 그려지는 부분 (파일의 구조나 레이아웃을 정의한다.)

- 기본 경로 : `앱 이름 / templates / 앱이름`  
  *템플릿 폴더의 이름은 반드시 'templates'라고 지정해야한다.

<img src=".\05. templates.png" style="zoom: 67%;"   >



>render 함수는 자동으로 'templates'라는 폴더를 찾아가서 템플릿을 찾음. 
>
>샌드위치 구조로 템플릿을 생성하는 이유는 만약 앱이 많아졌을 경우, 각 앱에서 `index.html`라는 중복된 이름의 템플릿을 사용하는 경우가 생긴다. 이 때 샌드위치 구조로 폴더를 구성해놓지 않으면 render 함수는 위에서 부터 차례대로 탐색을 하기 때문에 내가 사용하고자 하는 index.html 파일을 못찾을 수 있다!

 

`render(request, template_name, context)`

1. request : 응답을 생성하는데 사용되는 객체
2. template_name : 템플릿 전체 이름 또는 템플릿의 경로
3. context : 템플릿에서 사용할 데이터 (*딕셔너리 타입으로 작성) ; 꼭 딕셔너리 형태로만 넘겨줘야할까? 궁금하네요...



**Django Template Language (DTL)**

*주의! Python 코드로 실행되는 게 아님.

`{{variable}}`  : 변수 'dot(.)'을 이용하여 변수 속성에 접근할 수 있다. 

`{{variable|filter}}`  : 표시할 변수를 수정할 때 사용한다. 

`%tag%` : 변수보다 복잡한 작업을 수행한다. ex) `{%if%}{%endif%}`

`{# #}` : 한줄 주석, `{% coment %} {% endcoment %}` : 여러줄 주석



**Template Inheritance** (템플릿 상속)

템플릿 상속은 기본적으로 코드의 재사용성에 초점을 맞춘다.

skeleton 템플릿 (;뼈대가 되는 템플릿)을 통해서 모든 공통 요소를 포함하고 하위 템플릿이 재정의 (override) 할 수 있는 블록을 정의할 수 있다. 



템플릿 상속에 관련된 태그

`{% extends '' %}`  : 자식(하위) 템플릿이 부모 템플릿을 확장한다는 것을 알린다. (*반드시 템플릿 최상단에 작성되어야 한다. *2개 이상 사용할 수 없다.)



`{% block content %} {% endblock content %}` : 하위 템플릿에서 재지정(overridden) 할 수 있는 블록을 지정

`{% block content %} {% endblock %}` : 가독성을 높이기 위해서 선택적을 endblock 태그에 이름을 지정할 수 있다. 

 -> tag에 이름을 지정하는 이유는 멀까...? tag에 따라서 들어가는 위치가 달라지는 걸까?



>If you have app and project templates directories that both contain overrides, **the default Django template loader will try to load the template from the project-level directory first.** In other words, [`DIRS`](https://docs.djangoproject.com/en/4.1/ref/settings/#std-setting-TEMPLATES-DIRS) is searched before [`APP_DIRS`](https://docs.djangoproject.com/en/4.1/ref/settings/#std-setting-TEMPLATES-APP_DIRS). 
>
>: default는 pjt 레벨의 디렉토리에서 먼저 템플릿을 로드한다. APP_DIRS 보다 DIRS를 먼저 탐색한다.



1. 개별로 템플릿을 상속 받기

   `{% extends 'articles/base.html'%}`

2. 모든 앱에서 base.html을 상속 받기

   - base.html을 프로젝트 상단에 두기 : 프로젝트 폴더와 같은 층위에 `templates` 폴더 만들고 그 안에 base.html 작성하기
   - 프로젝트의 `settins.py`에 가서 `'DIRS' : [BASE_DIR / 'templates'],` 설정해주기 ; django에게 부모 템플릿인 base.html 여깄어! 하고 알려주는 거임
   - 필요한 템플릿의 상단에 `{% extends 'base.html'%}`  작성하기



<img src=".\10-1. base html.png">

1) 앱 외부에 templates 폴더 생성하고 그 아래에 skeleton 템플릿인 base.html을 만든다.
2) 상속받을 모든 하위 템플릿에 부트스트랩을 적용하기 위한 작업
3) 공통으로 사용할 내용을 작성하고 하위 템플릿에서 override 할 부분은 `{% block [name] %}`을 통해서 지정해준다. 



<img src=".\10-2. template inheritance.png">

프로젝트의  settings.py에 들어가서 템플릿 주소 지정해주기



<img src=".\10-3. template inheritance.png">

1) 상속 받을 템플릿 최상단에 `extends` 태그 작성해준다.
2) 하위 템플릿에서 보여줄 내용은 block 태그 내부에 작성해준다. 

왜 img 경로를 로컬로 하면 안되지..ㅠ html 공부하기..

<img src=".\10-4. result.png">





1. 상속 받은 부분
2. 하위 템플릿 내부 부분





---

### Django Design Pattern

**MTV 패턴**

>Django는 MVC (Model, View, Controller) 을 기반으로 한 MTV 패턴을 사용한다. 패턴에 따른 차이점은 없고 다만 일부 역할에 대해 부르는 이름이 다르다. 

- Mode - 데이터

  데이터와 관련된 로직을 관리한다.

  응용프로그램의 데이터 구조를 정의하고 데이터 베이스의 기록을 관리한다.



- Templates - 화면

  레이아웃과 화면을 처리한다.

  MVC 패턴에서 View의 역할을 담당한다. 



- View - 중간 처리 및 응답 반환

  Model과 Template과 관련한 로직을 처리하여 응답을 반환한다.

  클라이언트 요청에 대해 처리를 분기(; 명령 수행이 조건에 의하여 나뉘는 것)하는 역할

  MVC 패턴에서  Controller의 역할에 해당한다.

  

  <img src=".\06. django mtv.png" style="zoom: 80%;"> (출처: MDN)	









---

### MTV 구조와 CRUD

**Variable routing**

: URL 주소를 변수로 사용하여 view 함수의 인자로 넘길 수 있다. 

- 변수는 `<>` 에 정의하며 <u>view 함수의 인자로 할당</u>된다. (이해함?)
- Default 타입은 'string'이며 5가지 타입으로 명시할 수 있다. (str, int 등)
- variable routing으로 할당된 변수를 인자로 받고 템플릿 변수로 사용할 수 있다. 



**App URL mapping**

: 앱이 많아졌을 때, urls.py를 각 앱에 매핑하는 방법



만약 같은 이름이 겹친다면,

1. `from articles import views as articles_views`

2. **각각의 app 폴더 안에 urls.py를 작성한다.**

   (1) mypjt > urls.py  ; 프로젝트의 urls.py에서 여러 앱의 url을 관리한다. 

   - `from django.urls import path, include`  및
   - `path('articles/', include('articles.urls')),`

   (2) articles 앱 폴더 안에 `urls.py` 파일 만들기 ; 개별 앱에서 url을 관리한다. 

   (3) articles > urls.py

   - `from django.urls import path`
   - `from . import views`
   - `urlpatterns = []`



<img src=".\11-1. urls mapping.png">

프로젝트 내 urls.py 작성



<img src=".\11-2. urls mapping.png">

1) urls import 하기
2) urlpatterns 작성하기
3) views import 해주기 이 때 article 내부이기 때문에 from 뒤에 . 현재경로임을 표시해주면된다. 



**include 되는 앱의 urls.py에 urlpatterns가 작성되어 있지 않으면 에러가 발생하므로 빈리스트라도 작성되어 있어야한다!



`include()` : 다른 URLconf(app/urls.py)들을 참조할 수 있도록 돕는 함수



**Naming URL patterns**

: DTL의 태그 함수 중 하나인 URL태그(`{% url 'url_name' %}`)를 사용하여 "path()" 함수에 name 인자를 정의하여 사용할 수 있다.  ex) `path('dinner/, views.dinner, name='dinner,)`

-> view 함수와 템플릿에서 특정 주소를 쉽게 참조할 수 있도록 돕는다.

-> 만약 "index/" 의 주소를 사용했떤 모든 곳을 찾아서 변경해야하는 번거로움을 방지할 수 있다. 

<img src=".\12. url name.png">



url 태그 사용하기

`{% url '' %}` ; url 태그 : 주어진 url 패턴 이름 및 선택적 매개 변수와 일치하는 절대 경로 주소를 반환한다...? 엥

<img src=".\13-1. url tag.png">



<img src=".\13-2. url tag.png">



**URL namespace**

: URL namespace를 사용하면 서로 다른 앱에서 동일한 URL 이름을 사용하는 경우에도 이름이 지정된 URL을 고유하게 사용할 수 있다. 

`app_name = 'articles'`

<img src=".\14-1. url name.png">



URL tag의 변화

`{% url 'url_name' %}`  >>> `{% url 'app_name:url_name' %}`

*app_name을 지정한 이후에는 url 태그에서 반드시 `app_name:url_name`의 형태로만 사용해야한다. 그렇지 않으면 NoReverceMatch 에러가 발생한다. 

<img src=".\14-2. url name.png">





---

### Model & Model Form

#### **Client**

**HTML <form> element** 
: 사용자로 부터 할당된 데이터를 어디(action)로 어떤 방식(method)으로 보낼지.

- action : 입력 데이터가 전송 될 URL을 지정 (default는 현재 페이지의 URL)

- method : GET방식과 POST방식 (2가지)으로만 HTML form 데이터를 전송한다. 





**HTML <input> element**
: 사용자로부터 데이터를 입력받기 위해 사용한다. 

- type : default 값은 "text"

- id :

- name : form을 통해 제출(submit)했을 때, name 속성에 설정된 값을 서버로 전송하고 서버는 **name 속성에 설정된 값을 통해 사용자가 입력한 데이터 값에 접근**할 수 있다.  (이 말을 이제서야 이해했네..!)

  서버에 전달하는 파라미터(name은 key, value는 value)로 매핑
  
  

[throw.html 작성하기]<img src=".\15-1. form.png">

> 하.. html 공부 안해서.. 모름... 
>
> label의 for 와 input의 id를 통일해줘야댐 -> Throw라는 글자를 눌렀을 때 input 박스가 활성화 됨!
>
> name이 input 값을 받아서 request의 딕셔너리 형태로 데이터를 저장함 (name이 key가 되고 입력받은 data가 value로 지정되는 형식이다.)





[catch.html 작성하기]<img src=".\15-2. form.png">



**HTTP request method**

HTTP : HTML 문서와 같은 리소스(데이터, 자원)들을 가져올 수 있도록 해주는 프로토콜 (규칙, 규약)

HTTP Method 예시 : **GET**, POST, PUT, DELETE



- GET : 서버로 부터 정보를 조회하는데 사용한다. 데이터를 가져올 때만 사용해야한다. 

  데이터는 URL 포함되어 서버로 보내진다. 







**Query String Parameters**

사용자가 입력 데이터를 전달하는 방법 중 하나로써, url 주소에 데이터를 파라미터를 통해 넘기는 것이다. 

앰퍼샌드(&)로 연결된 `key=value&key=value` 쌍으로 구성된다. 기본 URL과는 물음표(?)로 구분된다. 

예시) `http://127.0.0.1:8000/articles/throw/?message=1시간만잘까#`

파라미터가 여러개일 경우에는 &를 붙여서 여러개의 파라미터를 넘길 수 있다. 



### Server

> GET 메서드를 이용하여 URL에 포함되어 서버에 전달된 데이터는 어떻게 접근할 수 있을까?
>
> ; view 함수에서는 어떻게 해당 데이터에 접근 할 수 있을까?

**request 객체**

: 모든 요청 데이터는 view 함수의 첫번째 인자 `request`에 들어있다. 



request는 어떤 객체인지 print를 통해서 알아보자! (throw.html에서 작성한 form 참조)

[catch 함수를 통해 결과확인(print)]<img src=".\16. request.png">

request를 프린트하면 url 주소로 입력된 값들이 전부 넘어오는구나

?  request.GET 이 뭘 불러오는 걸까? `.GET`의 용법이 어떤 거지? -> .GET을 통해서 name을 key : value를 data로 한 딕셔너리가 넘어온다. 

?? request.GET.get('message') 는 뭘 불러오는 걸까...................... `.get('message')` 딕셔너리 key값을 이용해서 value를 불러오는 거임 ; GET이 딕셔너리 형태로 넘어오니까



[catch 함수 완성하기]<img src=".\17-1. catch.png">

[catch.html 완성하기]<img src=".\17-2. catch.png">



---

--여기서 한 번 나눠서 프로젝트 파일 만들어야함--

djagno 모델을 공부하기 위해서, database 기초 용어는 알아야댐.

**Database**

1. 스키마 (Schema)

   : 뼈대 (Structure), 데이터베이스에서 자료의 구조, 표현방법, 관계 등을 정의한 구조?

   

2. 테이블 (Table)

   : 필드(열)과 레코드(행)를 사용해 조직된 데이터 요소들의 집합 (==관계;relation)

   1) 필드 (field) 

      : 속성 혹은 열(column)

      각 필드에는 고유한 데이터 형식이 지정된다. ex) int, text 등

   2)  레코드 (record) 

      : 튜플 혹은 행(row)

      테이블의 데이터는 레코드에 저장된다. 

      아래 예시의 경우 4개의 레코드가 존재한다. 

   3) PK (Primary Key) ; id열

      : 기본 키; 각 레코드의 고유한 값 (식별자로 사용)

      **다른 항목과 절대로 중복될 수 없는 단일 값(unique)**

   4) Query (쿼리)

      : 데이터를 조회하기 위한 명령어

      조건에 맞는 데이터를 추출하거나 조작하는 명령어 (주로 테이블형 자료구조에서)

      Query를 날린다 == 데이터베이스를 조작한다. 

   

   <img src=".\18. table.png">

   



### Django Model

> python의 class 공부 다시 해야함............

django는 model을 통해 데이터에 접근하고 조작

model == 저장된 데이터베이스의 구조(layout)

일반적으로 각각의 모델은 하나의 데이터베이스 테이블에 매핑(mapping)

​	-> 모델 클래스 1개 == 데이터베이스 테이블 1개 (이게 무슨 말일까......)



django는 웹 어플리케이션 데이터를 구조화하고 조작하기 위한 추상적인 계층(모델)을 제공한다. 

-> 모델을 통해서 데이터를 관리한다. 



**모델 작성하기**

- models.py 작성

  모델 클래스를 작성하는 것 == 데이터 베이스 테이블의 스키마(뼈대; 구조)를 정의하는 것

[models.py 작성하기]<img src=".\19. models.png">

> 1. crud 프로젝트 만들기
> 2. articles 앱 만들기
> 3. settings.py에 앱 등록하기
> 4. models.py 작성하기
>
> *id 칼럼은 테이블 생성하면 django가 자동으로 생성한다. 



**모델 이해하기**

각 모델은 django.models.Model 클래스의 서브 클래스 == django.db.models 모듈의 Model 클래스를 상속받아 구성된다! 



models 모듈을 통해서 어떤 타입의 DB필드(coloumn)을 정의한 것인가 정한다. 

- 클래스 변수(속성)명 : title, content ; DB 필드의 이름
- 클래스 변수 값 (models 모듈의 field 클래스) : modles.Textfield .. ; DB필드의 데이터 타입



django model field

- django는 모델 필드를 통해 테이블의 필드(칼럼)에 저장한 데이터 유형(int, txt 등)을 정의한다. 

- 데이터 유형에 따른 다양한 모델 필드를 제공한다. 

  ex) DataField(), CharField(), IntegerField

  [공식 문서 참조](https://docs.djangoproject.com/en/3.2/ref/models/fields/)

  

  - 사용한 모델 필드 알아보기 (이건 따로 한 페이지에 정리하면 좋을듯)

-- 여기까지 데이터베이스의 스키마 (골격)을 정의함 --

이후 이 모델의 변경사항을 실제 데이터베이스에 반영하기 위한 과정이 필요하다!



**Migrations**

django가 모델에 생긴 변화(필드 추가, 수정 등)를 실제 DB에 반영하는 방법

`python manage.py makemigrations` : 모델의 변경사항에 대한 새로운 migration을 만들 때 사용한다.

<img src=".\20-1. migration.png" style="zoom:50%;" >

<img src=".\20-2. migration.png" style="zoom:50%;" >

명령어 실행 후 `migrations/0001_initial.py`가 생성된 것을 확인 == 파이썬으로 작성된 '설계도'



`python manage.py migrate` : makemigrations으로 만든 설계도를 실제 데이터 베이스에 반영하는 과정 (db.sqlite3 파일에 반영) -> 결과적으로 **모델의 변경사항**과 **데이터베이스를 동기화**하는 과정! (만약 모델에 설정된 필드와 데이터베이스에 있는 데이터의 유형이 다르면..... 어떻게 되는 걸까)

[migrate하기 전 db가 비어있음]<img src=".\21-1 migrate.png" >

[migrate한 후 데이터 베이스에 동기화됨]<img src=".\21-2 migrate.png" >



기타 migrations 명령어

- `python manage.py showmigrations` : migrations 파일들이 migrate 됐는지 안됐는지 여부를 확인하는 용도 [X] 표시가 있으면 migrate가 완료됐다는 의미

  [migrate가 안된 상황]<img src=".\20-2. migration.png" >



makemigrations을 통해 만들어진 설계또는 파이썬으로 작성되어있다. 

-> SQL만 알아들을 수 있는 DB가 어떻게 이 설계도를 어떻게 이애하고 동기화를 이룰 수 있을까?

-> 이 과정에서 중간에 번역을 담당하는 것이 `ORM`



### ORM

Object-Relational-Mapping

객체 지향 프로그래밍 언어(e.g. 파이썬)를 사용하여 호환되지 않는 유형의 시스템 간의 데이터를 변환하는 프로그래밍 기술 

Django는 Dango ORM을 사용한다.  

== SQL을 사용하지 않고 데이터베이스를 조작할 수 있도록 만들어주는 매개체 (라잌.. 번연기?)



**사전준비**

vscode SQLite 확장 프로그램 설치하기 : 직접 테이블 데이터 확인가능

추가 라이브러리 설치

- `pip install ipython` 

  Ipython (Interactive Python) : 복수이 프로그래밍 언어에서 상호작용하는 컴퓨팅을 하기 위한 명령 셸. 인터프리터로 작동하는 파이썬 코드의 한계를 확장하여 리눅스의 쉘과 같이 이용할 수 있도록 기능이 추가된 파이썬. 

-  `pip install django-extension` : shell_plus 사용하기 위함

  장고의 기본명령 기능을 확장 + 부가기능 추가

  -> 패키지 목록 업데이트하기 `pip freeze > requirements.txt`

  

  [django-extensions 등록해주기]<img src="22-1. shell.png">

  등록안해주면 shell_plus 못씀

**Django shell**

ORM 구문 연습을 위해 파이썬 쉘 환경 사용

다만 일반 파이썬 쉘을 통해서는 장고 프로젝트 환경에 영향을 줄 수 없기 때문에 django환경 안에서 진행할 수 잇는 django shell을 진행

`python manage.py shell_plus` django-extenstion이 제공하는 더 강력한 shell_plus로 진행한다. (왜?)

[shell_plus 활성화된 화면]<img src="22-2. shell.png">



**QuerySet API**

Database API

django가 제공하는 ORM을 이용해 데이터 베이스를 조작하는 방법

model을 정의하면 데이터를 만들고 읽고 수정하고 지울(crud) 수 있는 API(Application Programming Interface; 응용프로그램과 운영체제의 통신을 쉽게하는 연결 인터페이스)를 제공한다. 

**database API 구문**

<img src="23-1 api.png">

- objects manager

  django 모델이 데이터 베이스 쿼리작업을 가능하게 하는 인터페이스

  django는 기본적으로 모든 django 모델 클래스에 대해  objects라는 manager 객체를 자동으로 추가한다. 

  -- DB를 Python Class로 조작할 수 있도록 여러 메서드를 제공하는 manager

- Query

  데이터 베이스에 특정한 데이터를 보여달라는 요청

  "쿼리문을 작성한다"

  -- 원하는 데이터를 요청하기 위해 데이터베이스에 보낼 코드를 작성한다. 

  이때, 파이썬으로 작성한 코드가 ORM에 의해 SQL로 변환되어 데이터 베이스에 전달되며, 데이터베이스의 응답 데이터를 ORM이 `QuerySet`이라는 자료형태로 변환하여 우리에게 전달한다. 

- QuerySet

  데이터베이스에게서 전달 받은 객체 목록(데이터 모음) ; 순회가 가능한 데이터로써 1개 이상의 데이터를 불러와 사용할 수 있음; 필터를 걸거나 정렬 등을 수행할 수 있다.

  --데이터베이스가 단일한 객체를 반환할 때는 QuerySet이 아닌 <u>모델(Class)의 인스턴스로 반환</u>됨 (???)

- QuerySet API

  QuerySet과 상호작용하기 위해 사용하는 도구 

---

### CRUD

**create**(생성)

데이터 객체를 만드는 3가지 방법

1. 첫번째 방법

   `article = Article()` : 클래스를 통한 인스턴스 생성

   `article.title` : 클래스 변수명과 같은 이름의 인스턴스 변수를 생성 후 값 할당

   `article.save()` : 인스턴스로 save 메서드 호출

   [첫번째 방법- 데이터 베이스와 shell_plus 창 확인하기]<img src=".\24-1. create.png">

   >.save() 해주지 않으면 DB에 값이 저장되지 않는다. 
   >
   >save 메서드를 호출해야 비로소 DB에 값이 저장된다. (레코드 생성)
   >
   >.save() 하기 전과 후의 데이터 베이스의 상태 비교하기

   <img src=".\24-2. create.png">

   > DB 테이블의 칼럼 이름이 id임에도 pk를 사용할 수 있는 이유는 django가 제공하는 shortcut이기 때문이다. 

   [인스턴스인 article을 활용하여 변수에 접근해보자! (데이터가 저장되었는지 확인)]<img src=".\24-3. create.png">



2. 인스턴스 생성 시 초기값을 함께 작성하여 생성한다 (권장)

   <img src=".\24-4. create.png">

   > article이란 동일한 변수를 사용한 탓에.. 재할당됨. 그래서 article의 값을 불러오면 마지막에 저장된 값들이 불려온다.

3. QuerySet API 중 create() method 활용

   <img src=".\24-5. create.png">

   > 권장하는 방법은 아님! save 메서드를 거치지 않고 바로 DB에 저장되기 때문에 위험함.

`.save()` (saving object) 

객체를 데이터 베이스에 저장한다.

데이터 생성 시 save를 호출하기 전 객체의 id 값은 



**read** (읽기)

QuerySet API method를 사용해 데이터를 다양하게 조회하기

-> 2가지로 분류된다. 

- return new querysets
- do not return querysets



`all()` 

- QuerySet return

- 전체 데이터 조회

  

`get()`

- 단일 데이터 조회

- 객체를 찾을 수 없으면, `DoesNotExist` 예외를 발생시킴

  둘 이상의 객체를 찾으면, `MultipleObjectsReturned` 예외를 발생시킨다.

  -> 이와 같은 특징 때문에 primary key와 같이 고유성(uniqueness)을 보장하는 조회에서 사용해야 한다. 

  

`filter()`

- 지정된 조회 매개 변수와 일치하는 객체를 포함하는 새로운 QuerySet을 반환한다. 

  *조회된 객체가 없거나 1개여도 QuerySet을 반환



**update**(수정)

과정

1. 수정하고자 하는 article 인스턴스 객체를 조회 후 반환 값을 저장

2. article 인스턴스 객체의 인스턴스 변수 값을 새로운 값으로 할당

3. save()

   <img src=".\25-1. update.png">



**delete** (삭제)

1. 삭제하고자 하는 article 인스턴스 객체를 조회 후 반환 값 저장

2. delete() 인스턴스 메서드 호출

   <img src=".\26-1. delete.png">



---

### HTTP Method

**Admin site**

django의 가장 강력한 기능 중 하나인 'automatic admin interface' 

== 관리자 페이지

- 사용자가 아닌 서버의 관리가가 활용하기 위한 페이지
- 모델 class를 admin.py에 등록하고 관리 (원래는 모델 등록하고 migrate 햇음..)
- 레코드 생성 여부 확인에 매우 유용 + 직접 레코드 삽입 가능



admin 계정 생성하기

`python manage.py createsuperuser`

<img src=".\27-1. admin.png">

> username과 password를 입력해 관리자 계정 생성
>
> email은 선택사항
>
> 비밀번호 생성 상 보안으로 인해 터미널에서 확인 불가능! 
>
> 비밀번호 너무 단순하다고 경고문 떴지만 걍 무시하고 y 하면 됨



/index/ 를 통해서 관리자 페이지 접속하기

<img src=".\27-2. admin.png">



<img src=".\27-3. admin.png">

> 계정만 만든 경우 django 관리자 화면에서 모델 클래스는 보이지 않는다.



admin에 모델 클래스 등록

-- 모델의 record를 보기 위해서는 admin.py에 등록해야한다.

<img src=".\27-4. admin.png">





admin 페이지에서 데이터 조작하기

<img src=".\27-5. admin.png">



<img src=".\27-6. admin.png">



결과 확인하기

<img src=".\27-7. admin.png">



---

**CRUD 구현하기**

사전준비

1) base.html -- bootstrap CDN 및 템플릿 추가 경로 작성

2) crud/urls.py -- articles/urls.py -- url 분리 및 연결

3) index 페이지 작성 -- urls.py > views.py > index.html

4) Article Model 작성 -- articles/models.py

   <img src=".\28-1. read.png">

   > Article 모델에 제목, 내용, 수정일, 작성일 포함..
   >
   > 모델을 만드는 이유가 뭔데?.. 클래스 만드는 거랑 똑같은 거지?



**READ**

INDEX 페이지

1. 전체 게시글 조회

   index 페이지에서 전체 게시글을 조회해서 출력한다.

   views.py

   <img src=".\29-1. index.png">

   >1. articles/models.py에 정의한 Article 모델을 가져온다.  
   >2. ORM언어를 통해 데이터 베이스에 접근
   >3. context에 담아서 딕셔너리 형태로 템플릿에서 사용할 데이터를 넘겨준다!

   index.html

   <img src=".\29-2. index.png">

   결과 확인

   <img src=".\29-3. index.png">

DETAIL 페이지

개별 상세 페이지 

모든 게시글마다 뷰함수와 템플릿 파일을 만들 수 없다.

글 번호 (pk)를 활용하여 하나의 뷰 함수와 템플릿 파일로 대응 -- Variable Routing 활용

1. urls

   url로 특정 게시글을 조회할 수 있는 번호를 받는다. 

   <img src=".\30-1. detail.png">

2. views

   <img src=".\30-2. detail.png">

   >오른쪽 pk는 variable routing을 통해 받은 pk
   >
   >왼쪽 pk는 DB에 저장된 레코드의 id 칼럼
   >
   >...하? 그래서 이게 먼가요
   >
   >그리고 왜 걍 article이라고 변수명을 지어서 날 헷갈리게 하나요?

3. detail.html

   <img src=".\30-3. detail.png">

   >작성햇고

4. 결과물

   <img src=".\30-4. detail.png">

영화 제목 누르면 상세 페이지로 넘어가도록 index.html 수정하기

1. index.html 수정

   <img src=".\30-5. detail.png">

   >url 'articles:detail' -> articles라는 앱네임의 views 함수인 detail 로 간다.
   >
   >article.pk 라는 인자와 함께 넘겨준다. 

2. 결과물

   <img src=".\30-6. detail.png">

   

**CREATE**

1. 사용자의 입력을 받을 페이지를 렌더링 하는 함수 : new

   1. urls.py

      <img src=".\31-1. new.png">

   2. views

      <img src=".\31-2. new.png">

   3. new.html

      <img src=".\31-3. new.png">

   4. 결과물

      <img src=".\31-4. new.png">

      

2. 사용자가 입력한 데이터를 전송받아 DB에 저장하는 함수 : create

   1. urls.py

      <img src=".\32-1. create.png">

   2. views.py

      <img src=".\32-2. create.png">

      >2번 데이터 생성하기의 경우 3가지 방법으로 가능하다 (ORM)
      >
      >그 중 가장 많이 쓰이는 2번째 방법으로 생성했음
      >
      >1번 혹은 2번 생성 방식을 사용하는 이유,
      >
      >- create 메서드가 더 간단해 보이지만 추후 데이터가 저장되기 전에 유효성 검사 과정을 거치게 될 예정
      >- 유효성 검사가 진행된 후에 save 메서드가 호출되는 구조를 택하기 위함

   

   create 함수를 통해서 데이터를 가져와 데이터베이스에 저장했다. 그럼 유저는 어디를 보게 해야할까? --> index, detail 등 이미 만들어져 있는 url로 보내면 된다. 

   

   **django shortcut function** : `redirect()`

   : 인자가 작성된 곳으로 다시 요청을 보낸다.

   인자

   1. view name (URL pattern name) : `return redirect('articles:index')`
   2. absolute or relative URL : `return redirect ('/articles/')`

   

   >render와 redirect의 차이점
   >
   >- render : 화면을 바로 그린다.  
   >- redirect : url로 보낸다. 

    3. form 마무리

       <img src=".\32-3. create.png">

       > new.html에서 form으로 받은 데이터를 articles의 create 함수로 보내준다!
       >
       > form action에 url 경로를 정해줌으로써 데이터를 보낼 곳을 지정해준다.

    4. 결과

       오류뜸. 해결은 그 다음 단계............



​	<img src=".\33-1. csrf.png">

















---

# 여기 아래는 정리해야됨..



'23 0321

- 

![image-20230321150435770](C:\Users\SSAFY\AppData\Roaming\Typora\typora-user-images\image-20230321150435770.png) 
return없이 redirect를 쓰면 이동할 url을 알려주기만 한다. 

![image-20230321150412862](C:\Users\SSAFY\AppData\Roaming\Typora\typora-user-images\image-20230321150412862.png)
 return redirect를 쓰면, 이동할 url로 바로 이동!



분기를 해준다. 

분기 ; 명령 수행이 조건에 의해 순차적인 정상 순위에서 벗어나는 것. 또는, 이러한 일을 수행하는 기계어.



![](C:\Users\SSAFY\AppData\Roaming\Typora\typora-user-images\image-20230321145115015.png)

(views.py)

에이든 교수님이 return 빼먹음!!!!!!!! 교안에 없으니까 잘 확인하기

![image-20230321145212575](C:\Users\SSAFY\AppData\Roaming\Typora\typora-user-images\image-20230321145212575.png)

(detail.html)

method 지정 안해주면 default가 GET이니까 POST요청으로 바꿔줘야함!!!!!



---

### Django Form

1차적 목표 : form을 너무 많이 작성해야하는 건 번거롭다. 나는 만들어진 템플릿의 form을 쓰고 싶다~~~~ 



2차적 목표 : 버그 덩어리...! 유효성 검사가 필요하다. > 장고가 대신 해준다. 



---

'23 0322 권한과 인증



pip install pillow << 이게 먼데...

사전 설정 따라하기 : 앱 accounts 등록하기



인증을 하려면, 유저라는 게 있어야 한다. 

유저모델 자체도 쟝고는 제공해주고 있다. 



![image-20230322111649808](C:\Users\SSAFY\AppData\Roaming\Typora\typora-user-images\image-20230322111649808.png)

> 적는 위치는 상관없음



프로젝트 중간에 AUTH_USER_MODEL 변경 Noooooo.. 프로젝트 처음에 진행하기!

필드 추가하는 건 나중에 해도 괜찮다. 



데이터베이스 초기화

- 쟝고를 가지고 프로젝트를 진행 .. 코딩하는데 1시간 에러 정리하는데 2시간 함.

데이터베이스 모델링이 꼬인 경우, 데이터 베이스 초기화 하고 다시 하는 게 좋음



1) init 파일만 남기고 삭제하면 됨
2) db도 삭제한다.
3) migrations 진행



auth_user가 아니라 acounts_user로 테이블이 변경된다. 



### HTTP

1. 비연결지향

   서버는 요청에 대한 응답을 보낸 후 연결을 끊는다. 요청에 대해 일일이 응답하고 끝냄. 프로세스가 뭔가 단순하네..

2. 무상태(stateless)

   연결이 끊어지는 순간 클라이언트-서버 간의 통신은 끝난다.

   클라이언트와 서버가 주고받는 메시지들은 서로 완전히 독립적이다. 



이러한 HTTP의 특징으로 인해 데이터를 기억해줘!!! 하는 기술들이 생겨남 > 쿠키와 세션



### 쿠키

쿠키 == data 조각 (http의 특징을 보완해주는 역할)

클라이언트 > 서버 : 쿠키 한 조각 같이 줌 (로그인 정보를 같이 담아서)

이후에 클라이언트가 서버에게 요청을 보낼 때, 쿠키를 항상 같이 보낸다. 

서버는 이 때 로그인 정보가 있는 클라이언트인지 확인(쿠기 열기) 한다.

정보를 계속 준다 == 연결 상태를 유지한다. 

- 쿠키를 통해 사용자의 로그인 상태를 유지할 수 있다. 




### 세션

중요한 정보들은 쿠키에 담아서 보내면 위험함..!

HTTP : 무상태, 비연결

쿠키에 유저에 대한 데이터를 쿠키에 담아서 보내면 위험함!
그래서 유저에 대한 데이터는 서버에 저장해놓고, 쿠키에는 작은 메모만 !

데이터베이스에 세션 테이블을 만들고 세션id-value 태그를 만들어 여기(value)에 민감한 정보를 담는다. > 쿠키에는 session id만 담는다! > 쿠키를 받으면 세션의 id값을 받고 세션 테이블에서 해당 id에 맞는 value를 찾는다.



### 로그인

세션을 만드는 과정이다. 

![image-20230322104800614](C:\Users\SSAFY\AppData\Roaming\Typora\typora-user-images\image-20230322104800614.png)

템플릿 변수인 {{user}}를 view에서 넘겨준 적이 없어도.. 쟝고 템플릿에서 기본적으로 제공해주는 것들 중에 하나이다. 템플릿에서 user라는 걸 너무 많이 사용하니까 세션과 쿠키를 이용하여 인증을 하고 있다면 사용 가능하다. 



### 로그아웃

클라이언트와 서버에 있는 세션을 삭제하는 것. (둘 다 삭제해야된다. )











git bash에서 vs code 열기

`code .` 입력하면 된다. 







---

- 가상환경 세팅하기

  `pip install pillow` : 이미지 분석 및 처리를 쉽게 할 수 있는 라이브러리(Python Imaging Library:PIL)

  

  에러 `no such table` : migrate해줘야댐

  

  애플리케이션 만들 때, 계정 관련된 어플을 만들 때는 `accounts`로 이름을 만든다. (암묵적 약속)



---

0323

데코레이터

/accounts/delete < 이 url로 들어오면 POST로 들어오든 GET으로 들어오든 다 views.delete가 작동한다.





---

###### 알아두면 편한 vs code 단축키

`ctrl + 백틱 ` : 터미널 창 열기

`ctrl + j` : 터미널 창 숨기기 (종료 아님)

`ctrl + b` : explorer 창 여닫기

`ctrl + w` : 작업 창 종료하기

`alt + shift + 방향키` : 코드 복제 및 생성



###### bash 명령어

`touch [파일명]` : 파일 생성하기

`mkdir [폴더명]` : 폴더 생성하기 (make directory)



---

vs code 설정

emmet 설정 : django-html  / html 추가하기

자동 줄바꿈 : 설정 - word wrap 켜주기

