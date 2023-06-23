## 크롤링


```python
# 크롤링 , 웹 스크래핑 : 웹에 있는 데이터를 가지고 온다!
```


```python
# 데이터를 가져오는 라이브러리 : requests
# 가져온 데이터를 가공하는 라이브러리 : beatifulsoul
```


```python
# 크롤링 대상 : https://paullab.co.kr/stock.html
```


```python
import requests
from bs4 import BeautifulSoup

response = requests.get('http://www.paullab.co.kr/stock.html')

response.encoding = 'utf-8'
html = response.text

soup = BeautifulSoup(html, 'html.parser')
```


```python
soup.title
```




    <title>Document</title>




```python
soup.select('.tables')
```




    [<div class="tables">
     <table class="border-style" summary="시가총액 정보">
     <tr>
     <th class="strong" scope="row">시가총액</th>
     <!-- 공백은 의도적으로 넣은 것입니다. -->
     <td class="strong"><em id="_market_sum">349조 2,323</em>억원</td>
     </tr>
     <tr>
     <th scope="row">
     <a class="link_site" href="#">시가총액순위<i class="fas fa-caret-right"></i></a>
     </th>
     <!-- 공백은 의도적으로 넣은 것입니다. -->
     <td>위니브월드 <em id="_market_sum">1</em>위</td>
     </tr>
     <tr>
     <th scope="row">상장주식수</th>
     <!-- 공백은 의도적으로 넣은 것입니다. -->
     <td><em id="_market_sum">5,969,782,550</em></td>
     </tr>
     </table>
     <table class="border-style" summary="업종상세 정보">
     <tr>
     <th class="strong" scope="row">현재가</th>
     <td class="strong"><em id="_market_sum">349조 2,323</em>억원</td>
     </tr>
     <tr>
     <th scope="row">52주 최고 <span class="bar">l</span> 최저</th>
     <td>
     <em>62,800</em>
     <span class="bar">l</span>
     <em>42,300</em>
     </td>
     </tr>
     <tr>
     <th scope="row">배당수익률 <span class="bar">l</span><span> 2019.12</span>
     <a alt="배당수익률 상세설명" class="help" href="#"><em>?</em></a>
     <div class="lyr_section" style="display:none">
     <div class="tooltip_lyr dividend_layer" id="helpPannel5">
     <strong>배당수익률 = (배당금 / 현재가) x 100</strong>
     <p>배당금은 최근 결산연도 기준의 중간배당을 포함한 총 배당금입니다.</p>
     <span class="arrow"></span>
     </div>
     </div>
     </th>
     <td>
     <em id="_dvr">2.42</em>%
                     </td>
     </tr>
     </table>
     <table>
     <tr>
     <th class="strong" scope="row">매출</th>
     <!-- <td>22조 1,250억원</td> -->
     <td class="strong">22,125,034,978,750원</td>
     </tr>
     <tr>
     <th scope="row">비용</th>
     <!-- <td>19조 2,238억원</td> -->
     <td>19,223,803,154,781원</td>
     </tr>
     <tr>
     <th scope="row">순익</th>
     <!-- <td><em id="_market_sum">2조 9,012억원</em></td> -->
     <td><em id="_market_sum">2,901,231,823,969원</em></td>
     </tr>
     </table>
     </div>]




```python
총액정보 = soup.select('.tables')
총액정보[0].select('table')
```




    [<table class="border-style" summary="시가총액 정보">
     <tr>
     <th class="strong" scope="row">시가총액</th>
     <!-- 공백은 의도적으로 넣은 것입니다. -->
     <td class="strong"><em id="_market_sum">349조 2,323</em>억원</td>
     </tr>
     <tr>
     <th scope="row">
     <a class="link_site" href="#">시가총액순위<i class="fas fa-caret-right"></i></a>
     </th>
     <!-- 공백은 의도적으로 넣은 것입니다. -->
     <td>위니브월드 <em id="_market_sum">1</em>위</td>
     </tr>
     <tr>
     <th scope="row">상장주식수</th>
     <!-- 공백은 의도적으로 넣은 것입니다. -->
     <td><em id="_market_sum">5,969,782,550</em></td>
     </tr>
     </table>,
     <table class="border-style" summary="업종상세 정보">
     <tr>
     <th class="strong" scope="row">현재가</th>
     <td class="strong"><em id="_market_sum">349조 2,323</em>억원</td>
     </tr>
     <tr>
     <th scope="row">52주 최고 <span class="bar">l</span> 최저</th>
     <td>
     <em>62,800</em>
     <span class="bar">l</span>
     <em>42,300</em>
     </td>
     </tr>
     <tr>
     <th scope="row">배당수익률 <span class="bar">l</span><span> 2019.12</span>
     <a alt="배당수익률 상세설명" class="help" href="#"><em>?</em></a>
     <div class="lyr_section" style="display:none">
     <div class="tooltip_lyr dividend_layer" id="helpPannel5">
     <strong>배당수익률 = (배당금 / 현재가) x 100</strong>
     <p>배당금은 최근 결산연도 기준의 중간배당을 포함한 총 배당금입니다.</p>
     <span class="arrow"></span>
     </div>
     </div>
     </th>
     <td>
     <em id="_dvr">2.42</em>%
                     </td>
     </tr>
     </table>,
     <table>
     <tr>
     <th class="strong" scope="row">매출</th>
     <!-- <td>22조 1,250억원</td> -->
     <td class="strong">22,125,034,978,750원</td>
     </tr>
     <tr>
     <th scope="row">비용</th>
     <!-- <td>19조 2,238억원</td> -->
     <td>19,223,803,154,781원</td>
     </tr>
     <tr>
     <th scope="row">순익</th>
     <!-- <td><em id="_market_sum">2조 9,012억원</em></td> -->
     <td><em id="_market_sum">2,901,231,823,969원</em></td>
     </tr>
     </table>]




```python
총액정보 = soup.select('#_market_sum')
총액정보[2].text
```




    '5,969,782,550'




```python
soup.script
```




    <script src="https://code.jquery.com/jquery-3.5.1.js"></script>



## 강의해답코드(권고x, 필요에따라)


```python
class Stock:
    def __init__(self, 날짜, 종가, 전일비, 시가, 고가, 저가, 거래량):
        self.날짜 = 날짜
        self.종가 = 종가
        self.전일비 = 전일비
        self.시가 = 시가
        self.고가 = 고가
        self.저가 = 저가
        self.거래량 = 거래량

    def 거래금액(self):
        return self.종가 * sefl.거래량
```


```python
import requests
from bs4 import BeautifulSoup

response = requests.get('http://www.paullab.co.kr/stock.html')

response.encoding = 'utf-8'
html = response.text

soup = BeautifulSoup(html, 'html.parser')
```


```python
시세정보 = soup.select('table.table.table-hover')[0].select('span')
거래량 = []

for i in range(6, len(시세정보), 7):
    print(시세정보[i])
    거래량.append(시세정보[i].text.replace(',', ''))
    
거래량
```


```python
html
```


```python
soup.title
```


```python
soup.select('.tables')
```


```python
총액정보 = soup.select('.tables')
총액정보[0].select('table')[0]
```


```python
총액정보 = soup.select('#_market_sum')
총액정보[2].text
```


```python
import requests
from bs4 import BeautifulSoup

response = requests.get('https://search.zum.com/search.zum?method=uni&option=accu&rd=1&query=%EC%B5%9C%EC%8B%A0%EC%98%81%ED%99%94&qm=f_typing.top')

response.encoding = 'utf-8'
html = response.text

soup = BeautifulSoup(html, 'html.parser')
```


```python
soup.select('p.title > span')
```


```python
for i in soup.select('p.title > span'):
    print(i.text)
```


```python
for i, j in enumerate(soup.select('p.title > span'), 1):
    print(i, j.text)
```


```python
for i in soup.select('.thumb > img'):
    print('https:' + i['src'])
```


```python
titles = []
for i in soup.select('p.title > span'):
    titles.append(i.text)

imgs = []
for i in soup.select('.thumb > img'):
    imgs.append('https:' + i['src'])
```


```python
with open("index.html", "w") as f:
    s = '<h1>영화순위</h1>'
    for title, img in zip(titles, imgs):
        s += f'<h2>{title}</h2>'
        s += f'<img src={img}>'
    f.write(s)
```

## 연습문제

* 제주코딩베이스캠프 연구원에 2019.09.24일 부터 2019.10.23일까지 거래된 거래총량을 구해주세요. (https://paullab.co.kr/stock.html)

### 여러분들이 푼 풀이


```python
import requests
from bs4 import BeautifulSoup
from datetime import datetime

def str_to_datetime(s, char):
    result = datetime.strptime(s.replace(char,''), '%Y%m%d')
    return result

response = requests.get('http://www.paullab.co.kr/stock.html')
response.encoding = 'utf-8'
html = response.text
soup = BeautifulSoup(html, 'html.parser')

start_date = datetime.strptime('20190924', '%Y%m%d')
end_date = datetime.strptime('20191023', '%Y%m%d')

researcher_datas = soup.select('body > .main')[1]
# 방법 1
# l = researcher_datas.select('tr > td')
# date_datas = [str_to_datetime(i.text, '.') for i in l[::7]]
# trade_count_datas = [i.text.replace(',', '') for i in l[6::7]]
# data_set = list(zip(date_datas, trade_count_datas))

# 방법 2
l = researcher_datas.select('tr')[1:]
data_set = []
date = datetime.now
trade_count = 0
for i in l:
    date = str_to_datetime(i.select('td:nth-child(1)')[0].text, '.')
    trade_count = int(i.select('td:nth-child(7)')[0].text.replace(',', ''))
    data_set.append((date, trade_count))

filtered_datas = list(filter(lambda x:x[0] >= start_date and x[0] <= end_date, data_set))
# 방법 1로 뽑을 때
# print(sum(map(lambda x:int(x[1]), filtered_datas)))
# 방법 2로 뽑을 때
print(sum(map(lambda x:x[1], filtered_datas)))

# 방법 3
# date = datetime.now
# total_trade_count = 0
# for i in l:
#     date = str_to_datetime(i.select('td:nth-child(1)')[0].text, '.')
#     if date < start_date or date > end_date:
#         continue
#     total_trade_count += int(i.select('td:nth-child(7)')[0].text.replace(',', ''))
# print(total_trade_count)
```


```python
import requests
from bs4 import BeautifulSoup

response = requests.get('https://paullab.co.kr/stock.html')

response.encoding = 'utf-8'
html = response.text

soup = BeautifulSoup(html, 'html.parser')
# nth-child(3)를 사용하는 방법
# 자손선택자 선택하는 방법
표 = soup.select('body div:nth-child(3) table tr')
#필요로 하는 연구원 테이블의 행들을 가져옴
거래총액=0
for data in 표[1:]: #맨 첫번째 행은 숫자가 아니므로 제외함
    항목 = data.select(".num") # 행에서 num 클래스 select
    거래총액+=int(항목[5].text.replace(',','')) #가장 마지막 값인 거래액을 더함
print(거래총액)
```


```python
from bs4 import BeautifulSoup
import requests
from datetime import datetime as dt

response = requests.get('http://paullab.synology.me/stock.html')

response.encoding = 'utf-8'
html = response.text

soup = BeautifulSoup(html, 'html.parser')

len = [int(i.text.replace(",","")) for i in soup.select('h2#제주코딩베이스캠프연구원 + h3 + table > tbody tr td:nth-child(7) span')]
trList = soup.select('h2#제주코딩베이스캠프연구원 + h3 + table > tbody tr')
# print(trList)
datas = [int(i.select('td:nth-child(7) span')[0].text.replace(",","")) for i in trList[1:]
if dt.strptime(i.select_one('td:nth-child(1) span').text,'%Y.%m.%d') >= dt.strptime("2019.09.24","%Y.%m.%d")
if dt.strptime(i.select_one('td:nth-child(1) span').text,'%Y.%m.%d') <= dt.strptime("2019.10.23","%Y.%m.%d")]
print(sum(datas))
```


```python
response = requests.get('http://paullab.synology.me/stock.html')

response.encoding = 'utf-8'
html = response.text

soup = BeautifulSoup(html, 'html.parser')
```

### 강사의 코드


```python
# 문제를 보면
# step 1. 어떤 자료 구조를 사용하여 이 문제를 풀어갈 것인지
#         저는 class를 선택
class Stock:
    def __init__(self,날짜, 종가, 전일비, 시가, 고가, 저가, 거래량):
        self.날짜 = 날짜
        self.종가 = 종가
        self.전일비 = 전일비
        self.시가 = 시가
        self.고가 = 고가
        self.저가 = 저가
        self.거래량 = 거래량

    def 거래금액(self):
        return self.종가 * self.거래량
```


```python
# step 2. 자료구조가 정해졌으면 함수 아키텍처를 어떤 구조로 가져갈지
#         각 함수에 들어가는 파라미터나 아규먼트도 고민을 해야 합니다.

from bs4 import BeautifulSoup
import requests

#1
def get_parsing_data():
    '''
    requests 모듈 사용해서 data를 가져와 bs4로 parsing해주는 함수
    '''
    pass

#2
def get_select_data():
    '''
    parsing된 데이터에서 목적에 맞는 데이터 추출
    '''
    pass

#3
def create_instance():
    '''
    데이터 추출한 것을 인스턴스로 생성
    '''
    pass

#4
def sum_data():
    '''
    인스턴스에서 필요 영역을 다 더할 수 있도록 하는 함수
    '''
    pass
```


```python
# step3 함수 코딩

from bs4 import BeautifulSoup
import requests

def get_parsing_data(url):
    response = requests.get(url)
    response.encoding = 'utf-8'
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')
    return soup

def get_select_data(data, name, location): #company name은 활용하지 않습니다.
    return data.select('body > .main > table')[0]

def create_instance(datalist, selecdata):
    # 날짜 구해주는 함수를 깜빡했는데
    # 그대로(슬라이싱으로) 진행하겠습니다.
    for i in selecdata.select('tr')[1:]:
        # print(i.select('td'))
        날짜, 종가, 전일비, 시가, 고가, 저가, 거래량 = i.select('td')
        # print(날짜.text.strip(), 
        #       종가.text.strip(), 
        #       전일비.text.strip(),
        #       시가.text.strip(), 
        #       고가.text.strip(), 
        #       저가.text.strip(), 
        #       거래량.text.strip())
        datalist.append(Stock(날짜.text.strip(), 
              종가.text.strip(), 
              전일비.text.strip(),
              시가.text.strip(), 
              고가.text.strip(), 
              저가.text.strip(), 
              거래량.text.strip()))
        # print(날짜, 종가, 전일비)

def sum_data():
    pass

soupdata = get_parsing_data('http://paullab.synology.me/stock.html')
selecdata = get_select_data(soupdata, 
                '제주코딩베이스캠프연구원', 
                'body > .main > table')
datalist = []
create_instance(datalist, selecdata)
datalist[0].종가
```

### 일반적인 풀이


```python
response = requests.get('http://paullab.synology.me/stock.html')

response.encoding = 'utf-8'
html = response.text

soup = BeautifulSoup(html, 'html.parser')

data = soup.select('body > .main > table')[0]

for i in data.select('tr')[1:]:
    for j in i.select('td'):
        print(j.text.strip())
    print('----')
```


```python
response = requests.get('http://paullab.synology.me/stock.html')

response.encoding = 'utf-8'
html = response.text

soup = BeautifulSoup(html, 'html.parser')

data = soup.select('body > .main > table')[0]

for i in data.select('tr')[1:]:
    print(i.select('td:nth-child(7)'))
```


```python
response = requests.get('http://paullab.synology.me/stock.html')

response.encoding = 'utf-8'
html = response.text

soup = BeautifulSoup(html, 'html.parser')

data = soup.select('body > .main > table')[0]

result = []
for i in data.select('tr')[1:]:
    result.append(int(i.select('td:nth-child(7)')[0].text.replace(',', '')))

sum(result)
```
