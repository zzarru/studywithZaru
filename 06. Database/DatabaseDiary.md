# Database Diary

zaru



[SQLite 홈페이지](https://sqlite.org/index.html)



### SQLite3 설치하기

> MacOS는 기본적으로 설치되어있다. 

Window 기준 (64bit)

1. [SQLite 홈페이지에서 Download 하기](https://www.sqlite.org/download.html)
   - 본인의 PC의 운영체제에 맞는 버전을 찾아 파일을 다운로드한다. 

<img src ="./1-1. sqlite.png">



2. C드라이브에 가서 `sqlite` 라는 이름의 폴더를 생성한다. 

   <img src ="./1-2. sqlite.png">

3. 폴더 안에 다운받은 걸 푼다.

   <img src ="./1-3. sqlite.png">

4. 환경 변수 편집하고

   <img src ="./1-4. sqlite.png" style="zoom:50%;" >

   <img src ="./1-5. sqlite.png">

   <img src ="./1-6. sqlite.png">

   <img src ="./1-7. sqlite.png">

   

5. `alias sqlite = "winpty sqlite3"` 입력하기

   `.code` 로 vscode 열어서 `.bashrc`에 아래 명령어 입력 후 저장 

   <img src ="./1-8. sqlite.png">

   alias [별명] = "명령어"

   `sqlite3` 입력했을 때 정상적으로 sqlite3 작동하는지 확인하기 (위치 상관 없음)



**SQLite3 사용하기**

1. SQLite3 실행화면<img src="./3-1. sqlite3.png" style="zoom:150%;" >

2. 데이터베이스 파일 열기

   <img src="./3-2. sqlite3.png" style="zoom:150%;" >

   >1번 방법을 사용하면 현재 폴더에 db가 없다면, 해당 이름(`mydb.sqlite3`)의 DB를 생성하고 열어준다. 
   >
   >2번 방법의 경우 sqlite3 명령어와 함께 바로 DB 파일을 열어볼 수 있으나 해당 DB가 존재하는 경우에만 DB를 열 수 있음. 

3. sqlite3 종료하기

   `.exit` , `.quit`



**CSV 파일을 SQLite 테이블로 가져오기**

1. DML.sql 파일 생성

   <img src="./3-3. sqlite3.png" style="zoom: 80%;" >

2. 테이블 생성하기

   ```sql
   CREATE TABLE users (
   first_name TEXT NOT NULL,
   last_name TEXT NOT NULL,
   age INTEGER NOT NULL,
   country TEXT NOT NULL,
   phone TEXT NOT NULL,
   balance INTEGER NOT NULL
   );
   ```

   <img src="./3-4. sqlite3.png" >

3. 데이터베이스 파일 열기

   `sqlite3 mydb.sqlite3`

4. 모드(.mode)를 csv로 설정

   `.mode csv`

5. .import 명령어를 사용하여  csv 데이터를 테이블로 가져오기

   `.import users.csv users`

   `.import [csv_file_name.csv] [table_name]  `

   <img src="./3-5. sqlite3.png" >



6. 결과 확인

   <img src="./3-6. sqlite3.png" >







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

<img src="2-2. create.png"  >

query 실행 후에 생기는 테이블 및 스키마 확인

<img src="2-3. create.png">



**SQLite DATA TYPES**

1) NULL

   정보가 없거나 알 수 없음을 의미 (missiong information or unknown)

2) INTEGER

   정수

3) REAL

   실수 (8바이트 부동 소수점을 사용하는 10진수 값이 있는 실수)

4) TEXT

   문자 데이터

5) BLOB (Binary Large Object)

   입력된 그대로 저장된 데이터 덩어리 (대용 타입이 없다.)

   바이너리 등 멀티미디어 파일

   e.g 이미지 데이턴

6. 참조

   - SQLite에는 별도의 Boolean 타입이 없다. 
     대신 Boolean 값은 정수 0(False)와 1(True)로 저장된다. 

   - SQLite에는 날짜 및 시간을 저장하기 위한 타입이 없다. 
     대신 built-in "Data and Time Functions"로 TEXT, REAL, INTEGER 값으로 저장할 수 있다. 

     [Date And Time Functions 공식문서](https://sqlite.org/lang_datefunc.html) 확인하기



**TYPE Affinity** (타입 선호도)

특정 컬럼에 저장된 데이터에 권장되는 타입

데이터 타입 작성 시 SQLite의 5가지 데이터 타입이 아닌 다른 데이터 타입을 선언한다면 내부적으로 각 타입의 지정된 선호도에 따라 5가지 선호도로 인식됨

1. INTEGER
2. TEXT
3. BLOB
4. REAL
5. NUMERIC (?.. 아까 없엇는디)

타입 선호도가 존재하는 이유

- 다른 데이터베이스 엔진 간으니 **호환성**을 최대화
- 정적이고 엄격한 타입의 SQL문을 SQLite에서도 사용하기 위함



**Constraints**

== 제약조건

입력하는 자료에 대한 제약을 정한다.  (제약에 맞지 않으면 입력이 거부된다.)

사용자가 원하는 조건의 데이터만 유지하기 위한 == 데이터의 무결성을 유지하기 위한 보편적 방법으로 테이블의 특정 컬럼에 설정하는 제약



데이터의 무결성

무결성 == 데이터의 정확성, 일관성을 나타낸다.

데이터 베이스 내의 데이터에 대한 정확성, 일관성을 보장하기 위해 데이터 변경 혹은 수정 시 여러 제한을 두어 데이터의 정확성을 보증하는 것



Constraints의 종류

1. NOT NULL

   컬럼이 NULL 값을 허용하지 않도록 지정한다.

   기본적으로 NOT NULL 제약 조건을 명시적으로 사용하는 경우를 제외하고는 NULL값을 허용한다. 

2. UNIQUE

   컬럼의 모든 갓ㅂ이 서로 구별되거나 고유한 값이 되도록 한다.

3. PRIMARY KEY

   테이블에서 행의 고유성을 식별하는데 사용하는 컬럼

   각 테이블에는 하나의 기본 키만 있다. 

   암시적으로 NOT NULL 제약조건이 포함되어 있다. 

   *주의 INTEGER 타입에만 사용 가능

4. AUTOINCREMENT

   사용되지 않은 값이나 이전에 삭제된 행의 값을 재사용하는 것을 방지한다. 

   INTEGER PRIMARY KEY 다음에 작성하면 해당 rowid를 재사용하지 못함

   django 에서 테이블 생성 시 id 컬럼에서 기본적으로 사용하는 제약 조건

5. ETC



rowid 특징

테이블을 생성할 때마다 rowid라는 암시적 자동 증가 컬럼이 생성된다.

테이블에 새 행을 삽입할 때마다 정수값 (64비트 부호있는 정수 값)을 자동으로 할당한다.

값은 1부터 시작한다.

데이터 삽입 시에 rowid 또는 INTEGER PRIMARY KEY 칼럼에 명시적으로 값을 지정하지 않을 경우 SQLite는 테이블에서 가장 큰 rowid보다 하나 큰 다음 순차 정수를 자동으로 할당한다. (AUTOCREMENT와 관계없이-- 이게 무슨 의미일까)



만약 INTEGER PRIMARY KEY 키워드를 가진 컬럼을 직접 만들면 이 컬럼은 rowid 컬럼의 별칭(alias)가 된다. -- 새 컬럼 이름으로 rowid에 액세스 할 수 잇으며 rowid 이름으로도 여전히 액세스 가능하다.

만약 데이터가 최대 값에 도달하고 새 행을 삽입하려고 하면 SQLite는 사용되지 않은 정수를 찾아 사용한다. -- 찾을 수 없으면 SQLite_FULL 에러가 발생한다. -- 일부 행을 삭제하고 새 행을 삽입하면 삭제된 행에서 rowid 값을 재사용



### Alter Table

기본 테이블의 구조를 수정(변경)

ALTER TABLE문

1. **Rename** a table (테이블명 변경)
   : `ALTER TABLE table_name RENAME TO new_table_name;`

2. **Rename** a column (컬럼명 변경)
   : `ALTER TABLE table_name RENAME COLUMN column_name TO new_column_name;`

3. **Add** a new cloumn to a table (새 컬럼 추가)
   : `ALTER TABLE table_name ADD COLUMN column_definition;`

   만약 테이블에 기존 데이터가 있을 경우 `Cannot add NOT NULL column with default value NULL` 에러가 발생한다. 

   -- 이전에 이미 저장된 데이터드릉ㄴ 새롭게 추가되는 컬럼에 값이 없기 때문에 NULL이 작성된다. 

   -- 그런데 새로 추가되는 컬럼에 NOT NULL 제약조건이 있기 때문에 기본 값 없이는 추가될 수 없다는 에러가 발생한 것.

   해결방법

   -- 다음과 같이 `DEFAULT` 제약 조건을 사용하여 해결할 수 있다. 

   ```sql
   ALTER TABLE new_contracts
   ADD COLUMN adderess TEXT NOT NULL DEFAULT 'no address';
   ```

   -- 이렇게 하면 address  컬럼이 추가되면서 기존에 있던 데이터들의 address 컬럼 값은 'no address'가 된다. (.....먼 말임?)

   -- DEFAULT 제약조건은 column 제약 조건 중 하나로써 데이터를 추가할 때 값으 생략하기 위해 기본 값을 설정한다.  [공식문서 확인하기](https://sqlite.org/syntax/column-constraint.html)

4. **Delete** a column (컬럼 삭제)
   : `ALTER TABLE table_name DROP COLUMN column_name;`

   단, 삭제하지 못하는 경우가 있다!  `Cannot drop UNIQUE cloumn: "column_name"`

   - 컬럼이 다른 부분에서 참조되는 경우

     -- FOREIGN KEY (외래 키) 제약조건에서 사용되는 경우

   - PRIMARY KEY인 경우

   - UNIQUE 제약 조건이 있는 경우



### Drop Table

```sql
DROP TABLE table_name;
```

존재하지 않는 테이블을 제거하면 `no such table: table_name` 오류가 발생한다. 

한번에 하나의 테이블만 삭제할 수 있다.

여러 테이블을 제거하려면 여러 DROP TABLE 문을 실행해야한다.

DROP TABLE 문은 실행 취소하거나 복구할 수 없음 -> 각별히 주의해서 수행해야한다!





### DML

Data Manipulation Language; 데이터 조작

csv (comma-seperated values) : 필드를 쉼표(,)로 구분한 텍스트 데이터 및 텍스트 파일

>; 구문마다 세미콜론으로 마침!!!!!! 표시해줘야함



**Simple query**

- SELECT statement

  특정 테이블에서 데이터를 조회하기 위해서 사용한다. 

  문법

  ```sql
  SELECT [Column_name] FROM [Table_name];
  ```

  - SELECT 절에서 컬럼 또는 쉼표로 구분된 컬럼 목록을 지정
  - FROM 절에서 데이터를 가져올 테이블을 지정

  다양한 절과 함께 사용할 수 있다.

  - `ODER BY`, `DISTICT`, `WHERE`, `LIMIT` , `LIKE`, `GROUP BY`

  [이름과 나이 조회]

  <img src="4-2. dml.png">

  

  테이블에 있는 모든 컬럼을 조회 == 모든 데이터 조회

  ```sql
  SELECT * FROM [Table_name]
  ```

  *(asterisk) == 모든 컬럼에 대한 shorthand(약칭)

  

  [전체 데이터 조회]

  <img src="4-1. dml.png">





- Sorting rows

  `ORDER BY` 절을 사용하기

  ```sql
  SELECT select_list FROM table_name ORDER BY column ASC, column_2 DESC;
  ```

  SELECT문에 추가하여 결과를 정렬한다.

  ORDER BY절은 FROM절 뒤에 위치한다.

  하나 이상의 컬럼을 기준으로 결과를 오름차순, 내림차순으로 정렬할 수 있다. 

  - ASC : 오름차순 (Default)
  - DESC : 내림차순

  [실습1]

  <img src="4-3. dml.png"  >

  [실습2]

  <img src="4-4. dml.png">

  > ORDER BY절은 하나 이상의 컬럼을 정렬할 경우 첫번째 열을 사용하여 행을 정렬하고, 그런 다음 두번째 컬럼을 사용하여 정렬되어 있는 행을 정렬하는 방식
  >
  >
  > 먼저 age를 기준으로 먼저 오름차순으로 정렬하고,
  >
  > 이 결과를 balance를 기준으로 내림차순으로 정렬한 것


  Sorting NULLs

  NULL의 정렬 방식

  SQLite는 NULL을 다른 값보다 작은 것으로 간주한다.

  즉, ASC를 사용하는 경우 결과의 시작 부분에 NULL이 표시되고 DESC를 사용하는 경우 결과의 끝에 NULL이 표시됨
  

- Filtering data

  데이터를 필터링하여 중복제거, 조건 설정 등 쿼리를 제어하기

  Clause (절)

  - SELECT DISTINCT

    조회 결과에서 중복된 행을 제거한다.

    ```sql
    SELECT DISTINCT select_list FROM table_name;
    ```

    DISTINCT절은 SELECT문에서 선택적으로 사용할 수 있는 절

    문법 규칙

    -- DISTINCT절은 SELECT 키워드 바로 뒤에 작성 (주의)

    [실습1]

    <img src="5-1. filtering.png">

    

    <img src="5-2. filtering.png">

    >각 중복을 따로 계산하는 것이 아니라 두 칼럼을 하나의 집합으로 보고 중복을 제거한다.

    참고

    -- SQLite는 NULL 값을 중복으로 간주한다.

    -- NULL 값이 있는 칼럼에 DISTINCT 절을 사용하면 SQLite는 NULL 값의 한 행을 유지한다. (... 먼말임)

    

  - WHERE

    ```sql
    SELECT column_list FROM table_name
    WHERE search_condition;
    ```

    조회 시 특정 검색 조건을 지정

    WHERE 절은 SELECT문 / UPDATE문 / DELETE문 에서 선택적으로 사용할 수 있는 절

    FROM 절 뒤에 작서한다.

    `WHERE left_expression COMPARISON_OPERATOR right_expression`

    (==`WHERE 왼쪽표현식 연산자 오른쪽표현식`)

    ```sql
    WHERE column_1 = 10
    WHERE column_2 LIKE 'Ko%'
    WHERE column_3 IN(1,2)
    WHERE column_4 BETWEEN 10 AND 20
    ```

    - 비교 연산자

      <> or != (이거 외에는 python문법이랑 같다.)

    - 논리 연산자

      일부 표현식의 truth를 테스트할 수 있다.

      1, 0 또는 NULL 값을 반환한다.

      ALL, AND, ANY, BETWEEN, IN, LIKE, NOT, OR 등

    

    [실습]

    <img src="5-3. filtering.png">

    

  - LIMIT

    ```sql
    SELECT column_list FROM table_name LIMIT row)count;
    ```

    쿼리에서 반환되는 행 수를 제한한다.

    SELECT문에서 선택적으로 사용할 수 있는 절

    row_count는 반환되는 행 수를 지정하는 양의 정수

    <img src="5-9. filtering.png">

    >`ORDER BY`를 먼저 작성해야함 (반대로 작성하면 오류난다.)
    >
    >`LIMIT` 절에 지정된 행 수를 가져오기 전에 결과를 정렬하기 때문에..

    <img src="5-10. filtering.png">

    `OFFSET` 키워드

    LIMIT절에서 OFFSET과 함께 사용하면 특정 지정된 위치에서부터 데이터를 조회할 수 있다. 

    <img src="5-11. filtering.png">

    >offset은 초과!!!!!!!!! 임 그래서 11번부터 조회하려면 11이 아니라 10 써줘야댐

  

  

  

  Operator

  - LIKE

    패턴 일치를 기반으로 데이터를 조회

    SELECT / DELETE / UPDATE문의 WHERE 절에서 사용한다.

    SQLite는 패턴 구성을 위한 두개의 와일드카드(wildcards)를 제공한다

    1. % (percent)

       0개 이상의 문자가 올 수 있음

    2. _ (underscore)

       단일(1개) 문자가 있음을 의미 (글자수가 정해져있음)

    <img src="5-4. filtering.png">

    

  - IN

    값이 값 목록의 값과 일치하는지 여부에 따라 true 또는 false를 반환한다,

    IN 연산자의 결과를 부정하려면 NOT IN 연산자 사용

    <img src="5-5. filtering.png">

    > 1) IN절을 사용한 방법
    > 2)  WHERE문만 사용한 방법

    <img src="5-6. filtering.png">

  

  - BETWEEN

    `WHERE test_expression BETWEEN low_expression AND high_expression`

    값이 값 범위에 있는지 테스트

    값이 지정된 범위 안에 있으면  True를 반환

    SELECT, DELETE, UPDATE문의 WHERE절에서 사용할 수 있다. 

    BETWEEN 연산자의 결과를 부정하려면  NOT BETWEEN 연산자를 사용한다,.

    <img src="5-7. filtering.png">

    <img src="5-8. filtering.png">