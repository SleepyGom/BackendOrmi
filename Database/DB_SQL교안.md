# 1.DB란?
    * DB란 컴퓨터 안에 기록된 문자 또는 숫자를 의미
    * 데이터의 집함을 DB라고 한다.


# 2. DB? RDB? DBMS? RDBMS?
    * 데이터 베이스를 효율적으로 관리하는 소프트웨어를 DBMS(데이터베이스 관리 시스템 : Database Management System) 이라고 한다.
    * 데이터를 표 형태로 구조적으로 관리하는 모델을 관계형 모델이라한다. -> Relational Model -> RDB
    * RDB를 관리하는 시스템을 RDBMS라고 한다.
    * RDBMS의 대표 소프트웨어 Oracle, DB2, SQL Server PostgreSQL, MySQL, SQLite 등이 있다.
    * SQL 이란? -> RDBMS의 데이터를 관리하기 위한 프로그래밍 언어


# 3. RDB의 구성요소
    * 행, 열, 가상 테이블(VIEW), 행의 주소(INDEX), 시퀸스(SEQUENCE, 고유번호 자동 생성), 객체의 별칭(시노임, SYNONYM)


# 4. SQL(Structured Query Language)
    * 스토리지 언어의 표준으로 DB를 사용하여 프로젝트를 한다면 다룰 줄 알아야한다.
    ```
    SELECT * FROM Customers;
    ```
    ## 4-1 명령어의 분류
        ### 데이터 조작어(DML)
            * SELECT
            * INSERT
            * UPDATE
            * DELETE
        ### 데이터 정의어(DDL)
            * CREATE DATABASE
            * CREATE TABLE
            * CREATE INDEX
            * ALTER DATABASE
            * ALTER TABLE
            * DROP TABLE
            * DROP INDEX
            * RENAME
            * TRUNCATE
        ### 데이터 제어어(DCL)
            * GRANT : 권한부여
            * REVOKE : 권한제거
        ### 트랜젝션 제어어(TCL)
            * COMMIT
            * ROLLBACK
            * SAVEPOINT


# 5. DATA 분석 과정
    5-1. 데이터 -> 목표데이터(Target Data) -> 전처리 데이터(Preprocessed Data) -> 데이터 반환(Transformed Data) -> 패던(Patteerns) -> 지식(Knowledge)

    5-2. 사전 데이터 분석 및 1~3번까지 단계가 전체 과정의 70 ~ 80%

# 6. 정형? 비정형? 데이터
    6-1 정형 -> 테이블 안에 들어가 형식이 잡혀있는 데이터
        * 주로 숫자로 이루어진 데이터
        * 행렬 구조를 가지며, 연산이 가능하고, 일관성을 가진다.
    
    6-2 반정형 -> 스키마 구조 형태를 가지고 있는 데이터
        * 메타 데이터 포함, 값과 형식이 일관 x 연산x

    6-3 비정형 -> 정의된 데이터 모델이 없거나, 정의된 방식으로 정리 되지 않는 정보
        * 구조가 정해지짖 않은 데이터
        * 연산 x


# 7. CRUD
    * C -> Create
    * R -> Read
    * U -> Update
    * D -> Delete


# 8. 실습을 위한 데이터 세트 준비
    8-1 DBeaver 설치

    8-2 데이터베이스 선택
    ![selecting Database](./img/Database_select.png)

    8-3 SQL 선택
    ![selecting SQL](./img/selecting_SQL.png)

    8-4 setting
        * Server Host, Databse, UserName, Password, Port 설정
    ![setting](./img/setting.png)


# 9. SElECT, FROM
    9-1 SQL 쿼리를 입력하고, 결과 조회
        * SELECT 문을 이용해 DB에 있는 데이터 조회
        ```
        select 1;
        ```
        * 숫자를 그대로 출력 가능
        * 연산자 사용 가능(+, -, *, /) // 우선순위가 켜진다. ( 곱하기 -> 나누기 -> 나머지가 먼저 연산된다.)

        * 문자열을 그대로 출력 가능, 문자열 더하기
            * select 'hello world'; -> hello world 출력
            * select 'hello' + 'world'; -> x 문자열은 더하기가 되지않는다.
            * 문자열을 더하고 싶으면 select 'hello' || 'world';
        
        * 전체 정보 출력하기
            * select * from data;
        * 특정 column 선택하기
            * first_name을 선택하고 싶으면
            * selcet first_name * users;
        * 여러개 column 선택하기
            * select id, first_name, last_name from users;


# 10. AS
    10-1 AS란?
        * 해당 컬럼의 이름을 다시 정해서 나타내는 기능
        * 주로 식으로 된 컬럼의 컬럼명을 설정 OR 기존의 컬럼명을 간결하게 보여주기 위해 사용
        ```
        select name as product_name
        from products
        ```
        * 테이블 명 지정
        ```
        select
            a.id,
            a.name
        from products as a
        ```


# 11. LIMIT
    11-1 LIMIT이란?
        * 조회한 레코드 결과의 수를 제한한다.
        * LIMIT 없이 조회하면 모든 데이터를 조회하지만, LIMIT을 이용하면 원하는 갯수만큼 가지고 올 수 있다.
        ```
        select * from users limit 5;
        ```

        ```
        select *
        form products
        limit 3;
        ```


# 12. DISTINCT
    12-1 DISTINCT란?
        * 결과에서 중복된 행을 제거한다.
        ```
        select distinct country
        from users
        ```


# 13. WHERE
    13-1 WHERE 이란?
        * 원하는 데이터만 필터링한 결과를 조회
        * 여러 연산자를 결합하여 사용 가능
        * 비교연산자(=, <, >, !=, >=, <=), SQL연산자(BETWEEN), 논리 연산자(AND, OR) 등 사용가능
        ```
        SELECT *
        FROM users
        WHERE first_name = 'Michael';
        ```


# 14. SQL 연산자
    14-1 논리 연산
        * 우선순위는 NOT, AND, OR
        * AND - 모든 조건을 만족한 레코드를 조회
            ```
            select * from users
            where id < 10000
            and first_name = 'David'
            ```
        * OR - 조건을 하나라도 만족하면 레코드 조회
            ```
            select * from users
            where age < 20
            or age > 60
            ```

            ```
            select * from users
            where first_name = 'David'
            and (age < 20 or age > 60)
            ```
        * NOT - 조건 값이 아닌 레코드 전체 조회
            ```
            select * from users
            where NOT(country = "United States')
            ```

            ```
            select * from users
            where NOT (country = 'United States' or country = 'Brasil);
            ```

    14-2 BETWEEN 연산
        * between A AND B : A 와 B를 포함한 사이의 값을 조회
            ```
            select *
            from users
            where create_at between '2020-01-01' and '2020-02-01'
            ```

    14-3 IN 연산
        * IN A : A 안에 값과 일치하는 값을 조회
            ```
            select *
            form products
            where brand in ('Onia', 'Hurley', 'Matix')
            ```

    14-4 LIKE 연산
        * LIKE - '비교문자'
        * 비교 문자와 형태가 일치 (%(모든문자),_(한글자)사용)
        * 대소문자를 안가린다.
        * % 는 와일드 카드
            ```
            select *
            from products
            where name like '% Young %'
            ```

    14-5 IS NULL
        * NULL 값을 갖는 값(0은 값이 있는 것이다.)
            ```
            select *
            from order_items
            where shipped_at IS NULL;
            ```

            ```
            select *
            from order_items
            where shipped_at IS NOT NULL
            ```
        * 참고사항 - NULL(빈값) !='NULL(문자값)' 서로 타입이 다르다


