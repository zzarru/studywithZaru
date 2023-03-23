# Django Diary

###### Django 뿌신다.

작성자 : zaru



[Django 공식문서 바로가기](https://docs.djangoproject.com/en/4.1/)



### 기본 설정

**가상환경 세팅하기**

`python -m venv [가상환경 이름]` : 가상환경 설치하기. 

이 때, 가상환경 이름은 똑같이 'venv'로 지정하여 사용한다. (권장사항)

> `-m`  : 모듈을 탐색하거나 실행하거나 한다. 

`source venv/Scripts/activate` (winOS) / `source venv/bins/activate` (MacOS) : 가상환경 실행하기

-- 가상화면 실행 결과 확인하기 : (venv)가 떠있으면 가상환경 실행된 거임 --

![01 가상환경 세팅](C:\Users\SSAFY\Desktop\DjangoDiary\capture\01 가상환경 세팅.png)

`deactivate` : 가상환경 비활성화



**pip 설치하기**

###### ! pip란 파이썬으로 작성된 패키지 소프트웨어를 설치 및 관리하는 시스템이다. 

`pip list` : 설치된 pip 목록을 볼 수 있다. 

`pip django==3.2.18` : 버전을 명시하지 않으면 가장 최신 버전이 설치된다. 

`pip freeze > requirements.txt` : 가상환경 패키지 목록 저장 

`pip install -r requirements.txt` : 가상환경 패키지 설치



**Django 프로젝트 만들기**

`django-admin startproject [프로젝트 이름] .` 

*프로젝트 이름 뒤에 .을 찍으면 알아서 풀리고 .을 안찍으면 project 폴더 안에 새로운 project 폴더를 생성한다. (폴더 안에 풀기) ; 이름이 낭비되기 때문에 기본적으로 .을 찍고 프로젝트를 만든다. 

![02 django 프로젝트 만들기](C:\Users\SSAFY\Desktop\DjangoDiary\capture\02 django 프로젝트 만들기.png) 프로젝트를 생성하면 manage.py가 자동으로 만들어진다. 

> `manage.py` : django 프로젝트와 소통하는 유틸리티
>
> 사용법 : `python manage.py <command> [options]` 
>
> 

서버 실행하기 : `python manage.py runserver`

<img src="C:\Users\SSAFY\Desktop\DjangoDiary\capture\03 서버 실행하기.png" alt="03 서버 실행하기" style="zoom: 50%;" /> `ctrl + 서버주소 클릭` 하면 서버 페이지 확인 가능하다. 



![03-2 db 파일 생성](C:\Users\SSAFY\Desktop\DjangoDiary\capture\03-2 db 파일 생성.png) runserver 하고 나면 자동으로 `db.sqlite3` 이 생성된다. 



**Django 애플리케이션(앱) 생성하기**

`python manage.py startapp [앱 이름(복수형)]` : 일반적으로 앱 이름은  **복수형**으로 작성(권장)

> `django-admin startapp [앱 이름]` 으로도 앱을 생성할 수 있지만 권장하는 방식은 아니다. 

*앱(App) : 하나의 큰 기능 단위

**정해진 규칙은 없으며 개발자가 판단하여 앱을 생성한다. 



 **어플리케이션 등록하기**

앱을 사용하기 위해서 `settings.py` 의 INSTALLED_APPS 리스트에 반드시 추가해야한다. 

![04 앱 등록](C:\Users\SSAFY\Desktop\DjangoDiary\capture\04 앱 등록.png)

! 주의 'articles' 뒤에 , 빼먹지 않기! 



>프로젝트 vs 어플리케이션
>
>settings.py의 유무로 프로젝트와 어플리케이션을 구분한다. 어플리케이션의 경우에는 settings.py가 없다. 







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

