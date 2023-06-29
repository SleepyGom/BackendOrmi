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