# Database Diary

zaru

### SQLite3 설치하기

> MacOS는 기본적으로 설치되어있다. 

Window 기준 (64bit)

1. [SQLite 홈페이지에서 Download 하기](https://www.sqlite.org/download.html)
   - 본인의 PC의 운영체제에 맞는 버전을 찾아 파일을 다운로드한다. 

<img src ="./1-1. sqlite.png">



2. C드라이브에 가서 `sqlite` 라는 이름의 폴더를 생성한다. 
3. 폴더 안에 다운받은 걸 푼다.
4. 환경 변수 편집하고
5. `alias sqlite = "winpty sqlite3"` 입력하기



### 데이터베이스 (Database)

> "A database is an organized collection of data"



**DBMS** (Database Management System)

: 데이터 베이스에서 필요한 데이터를 잘 꺼내 쓸 수 있게 하는 프로그램; 데이터베이스를 조작하는 프로그램



**데이터베이스의 종류**

> SQL (관계형 데이터베이스) vs No SQL (비관계형 데이터베이스)

- 관계형 데이터베이스 (SQL == Relational Database)

  -- 표 형식으로 된 데이터베이스

  -- SQLite / MySQL / Oracle 등



### SQL

> Structured Query Language
>
> 관계형 데이터베이스에서 데이터를 관리하기 위해 사용하는 언어
>
> == 데이터베이스 관리 + CRUD하는 언어



**SQL Commands**

종류

1. **DDL** (Date Definition Language) : 데이터 정의 언어

   관계형 데이터베이스 구조(스키마, 테이블)를 정의하기 위한 명령어

   -- CREATE(생성), ALTER(수정), DROP(삭제) --

2. DML (Data Manipulation Language) : 데이터 조작 언어

   -- INSERT(추가), SELECT(조회), UPDATE(변경), DELETE(삭제) --

3. DCL (Data Control Language) : 데이터 제어 언어 

   ~~(지금 단계에서는 몰라도 됨)~~



SQL Syntax

- 모든 SQL문은 `키워드` 로 시작하고 `세미콜론(;)` 으로 끝난다.

  세미콜론은 각 SQL문을 구분하는 표준 방법

- SQL 키워드(e.g. SELECT, INSERT, UPDATE)는 대소문자를 구분하지 않는다.

  즉, SELECT로 작성하든 select로 작성하든 SQL문에서는 동일한 의미다.

  하지만 대문자로 작성하는 것을 권장 (가독성..때문에?)



- 참고

  - Statement (문)

    독립적으로 실행할 수 있는 완전한 코드 조각

    statement는 clause로 구성된다.

  - Clause (절)

    statement의 하위 단위

  - 예시 `SELCET column_name FROM table_name;`

    1개의 SELECT statement 는

    2개의  `SELECT column_name` 과 `FROM table_name`  clause로 구성되어있다. 

    

### DDL

Data Definition Language



**CREATE** TABLE statement

```sql
CREATE TABLE table_name (
column_1 data_type constraints,
column_2 data_type constraints,
column_3 data_type constraints
)
```

contacts 테이블 생성

Query 실행하기

실행하고자 하는 명령문에 커서를 두고 마우스 우측 버튼 -> Run Selected Query 클릭

<img src="2-2. create.png">

query 실행 후에 생기는 테이블 및 스키마 확인

<img src="2-3. create.png">











### DML

Data Manipulation Language; 데이터 조작

csv (comma-seperated values) : 필드를 쉼표(,)로 구분한 텍스트 데이터 및 텍스트 파일

>; 구문마다 세미콜론으로 마침!!!!!! 표시해줘야함



**Simple query**

- `SELECT [Column_name] FROM [Table_name];`

  데이터 조회할 때 사용

  문법 규칙

  - SELECT 절에서 컬럼 또는 쉼표로 구분된 컬럼 목록을 지정
  - FROM절(clause)에서 데이터를 가져올 테이블을 지정

- Select statement





`WHERE 왼쪽표현식 연산자 오른쪽표현식` 그렇군..





