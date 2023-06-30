# 1. 회원(users) 테이블의 모든 데이터를 조회하세요.
'''
select * from users
'''

# 2. 상품정보(products) 테이블의 모든 데이터를 조회하세요.
'''
select * from products
'''

# 3. 회원(users) 테이블의 이름(first_name), 성(lastname), 이메일(email), 국가 정보(country)를 조회하세요.
'''
select 
    first_name,
    lastname,
    email,
    country
from users
'''

# 4.(도전) 상품정보(products) 테이블의 id, 카테고리(category), 이름(name), 판매가격(retail_price), 비용(cost), 판매이익(판매가격 - 비용)을 조회하세요.
'''
select
    id,
    category,
    name,
    retail_price,
    cost,
    retail_price - cost
from products
'''

# 5. 상품정보(products) 테이블에서 5개 레코드만 조회하세요.
'''
select *
from products
limit 5;
'''

# 6. 회원(users) 테이블에서 이메일 주소(email) 20개를 조회하세요
'''
select email
from users
limit 20;
'''

# 7. 상품정보(products) 테이블에서 카테고리(category)를 중복제거하여 아래와 같이 조회하세요.
'''
select distinct category
from products
'''

# 8.(도전) 상품정보(products) 테이블에서 id, 카테고리(category), 이름(name), 판매가격(retail_price), 비용(cost), 판매이익(판매가격 - 비용), 수익율을 조회하세요.
# 각 컬럼의 이름은 다음과 같이 표현합니다.

# - id → product_id
# - 카테고리 → product_category
# - 상품명 → product_name
# - 판매가격 → product_price
# - 비용 → product_cost
# - 판매이익 → product_profit
# - 수익율 → product_profit_rate

'''
select
    id as product_id,
    category as product_category,
    name as product_name,
    retail_price as product_price,
    cost as product_cost,
    retail_price - cost as product_profit,
    (retail_price - cost) / cost * 100 as product_profit_rate
from products;
'''
### where 연습문제
# 9. 상품정보(products) 테이블에서 카테고리(category)가 ‘Swim’ 인 레코드의 모든 항목를 조회하세요.

'''
select category
from porducts
where category = 'Swim'
'''

# 10. 상품정보(products) 테이블에서 브랜드(brand)가 ‘2EROS’인 레코드의 id, 비용(cost), 브랜드(brand)를 조회하세요. 

'''
select 
    id,
    cost,
    brand
from products
where brand = '2EROS'
'''

# 11. 상품정보(products) 테이블에서 비용(cost)이 30이하이고 상품대상, 구분, 분야(department)이 ‘Men’인 모든 레코드를 10개를 조회하세요

'''
select  *
from products
where department = 'Men'
and cost <= 30
limit 10
'''

# 12. 상품정보(products) 테이블에서 
# 판매가격(retail_price)이 40이상인 레코드들의 
# 카테고리(category) 속성값을 
# 중복제거(distinct)하여 조회하세요.

'''
select distinct category
from products
where retail_price >= 40
'''

# 13. 상품정보(products) 테이블에서 비용(cost)이 50이상이고 70이하인 모든 레코드들 조회하세요.

'''
select *
from products
where cost between 50 and 70
'''

### 함수

# 15. 회원(users) 테이블에서 전체 유저의 평균연령을 조회하세요.

'''
select 
	avg(age)
from users
'''

# 16. 회원(users) 테이블에서 여성 유저의 평균연령을 조회하세요.
'''
select
    avg(age)
from users
where gender ='F'
'''

### GROUP BY
# 17. 회원(users) 테이블에서 국가별 가입자수를 조회하세요
'''
select
    country,
    count(id)
from users
group by country
'''

# 18. 회원(users) 테이블에서 남성 유저의 국가별 가입자 수를 조회하세요.
'''
select
    country,
    count(id),
from users
where gender = 'M'
group by country
'''

# 19. 회원(users) 테이블에서 
# 가입기간(created_at)이 2020년도 1월인 유저의 
# 국가별 가입자 수 (country_user_count)를 조회하세요.
'''
select
    country,
    count(id)
from users
where created_at >= '2020-01-01'
and created_at <= '2020-02-01'
group by country
'''

# 20. 회원(users) 테이블에서 가입기간(created_at)이 2020년도 1월인 유저의 
# 국가별 성별 가입자 수(country_gender_user_count)를 조회하세요.

'''
select
    country,
    gender,
    count(id)
from users
where created_at >= '2020-01-01'
and created_at <= '2020-02-01'
group by country , gender
'''

# 21. 주문정보(orders) 테이블에서 
# 주문생성일이 2022년도인 주문중에서
# 주문 상태가 환불(Returned)상태인 주문을 기준으로
# 유저 아이디(user_id)별 총 주문 아이템(num_of_item)의 합계를 조회하세요.

'''
select 
	user_id,
	sum(num_of_item) 
from orders
where status = 'Returned'
and shipped_at >= '2022-01-01'
and shipped_at <= '2023-01-01'
group by user_id
'''

### 정렬

# 1. 회원 테이블(users)에서 국가별 유저수를 조회하세요. 

# - 조회 항목 : 국가명(country), 국가별 유저수(user_count)
# - 조건 : 국가의 유저수가 3000명 이상인 국가
# - 정렬 : 국가별 유저수 많은순으로 정렬

'''
select
    country,
    count(id) as user_count
from users
group by country
having count(id) >= 3000
order by user_count desc
'''

# 2. 상품정보(products) 테이블에서 여성 스웨터중 판매가격이 제일 저렴한 5개를 조회하세요.

'''
select
    *
from products
where category = 'Sweaters'
and department = 'Women'
order by retail_price asc
limit 5
'''

# 3. 상품정보(products) 테이블에서 여성 스웨터의 브랜드별 평균 판매가격이 100이하인 브랜드의 브랜드 이름과 여성스웨터 평균판매가격을  조회하세요.

'''
select
    brand,
    avg(retail_price) as avg_retail_price
from products
where category = 'Sweaters'
and department = 'Women'
group by brand
having avg(retail_price) <=100
order by avg(retail_price) asc
'''

# 4. 상품정보(products) 테이블에서 각 제품의 id, 이름, 카테고리, 브랜드, 비용(cost), 판매가(retail_price), 이익금액(profit), 이익율(profit_rate)을 조회하세요.

'''
select
    id,
    name,
    category,
    brand,
    cost,
    retail_price,
    retail_price - cost as profit,
    (retail_price - cost) / retail_price * 100 as profit_rate,
from products
'''

# 5. # 상품정보(products) 테이블에서 수영카테고리 제품의 각 브랜드별 최소이익율, 최대 이익율, 평균 이익율을 조회하세요

'''
select
    brand,
    max((retail_price - cost) / retail_price * 100) as max_profit_rate,
    min((retail_price - cost) / retail_price * 100) as min_profit_rate,
    avg((retail_price - cost) / retail_price * 100) as avg_profit_rate
from products
where category = 'Swim'
group by brand
'''

# 6. 연습문제 5-5 데이터에서 평균이익율이 높은 TOP 5 브랜드와 평균이익율을 조회하세요.
'''
select
    brand,
    max((retail_price - cost) / retail_price * 100) as max_profit_rate,
    min((retail_price - cost) / retail_price * 100) as min_profit_rate,
    avg((retail_price - cost) / retail_price * 100) as avg_profit_rate
from products
where category = 'Swim'
group by brand
order by avg_profit_rate desc 
limit 5
'''

# 7. 상품정보(products) 테이블에서 카테고리 별 남성 제품의 수를 조회하세요. 
# - 조회 항목 : 카테고리, 제품의 수
# - 조건 : 카테고리 중 ‘Sport’가 들어가지 않은 카테고리, 남성 제품
# - 정렬  : 제품의 수가 많은 순으로 정렬

'''
select
	count(id),
	category
from products
where department = 'Men'
group by category 
having category not like '%Sport%'
order by count(id) desc
'''