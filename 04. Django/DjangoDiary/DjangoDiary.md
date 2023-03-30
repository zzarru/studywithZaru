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
3. context : 템플릿에서 사용할 데이터 (*딕셔너리 타입으로 작성)



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

- name : form을 통해 제출(submit)했을 때, name 속성에 설정된 값을 서버로 전송하고 서버는 name 속성에 설정된 값을 통해 사용자가 입력한 데이터 값에 접근할 수 있다. 

  서버에 전달하는 파라미터(name은 key, value는 value)로 매핑



**HTTP request method**

HTTP : HTML 문서와 같은 리소스(데이터, 자원)들을 가져올 수 있도록 해주는 프로토콜 (규칙, 규약)

HTTP Method 예시 : GET, POST, PUT, DELETE



**Query String Parameters**

사용자가 입력 데이터를 전달하는 방법 중 하나로써, url 주소에 데이터를 파라미터를 통해 넘기는 것이다. 

앰퍼샌드(&)로 연결된 `key=value&key=value` 쌍으로 구성된다. 기본 URL과는 물음표(?)로 구분된다. 

예시) `http://127.0.0.1:8000/articles/throw/?message=1시간만잘까#`



### Server

**request 객체**

: 모든 요청 데이터에는 view 함수의 첫번째 인자 `request`에 들어있다. 



 

---

# 여기 아래는 정리해야됨..



'23 0321

render와 redirect의 차이점

- render : 화면을 바로 그린다.  
- redirect : url로 보낸다.

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
