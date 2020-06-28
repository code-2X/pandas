#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas


# In[8]:


df = pandas.read_csv('data/gapminder.tsv', sep='\t')
# 데이터 집합을 불러오려면 read_csv 메서드를 사용해야 합니다.
# read_csv 메서드는 데이터 집합을 읽어 들여와 데이터프레임이라는 자료형으로 반환


# In[5]:


print(df.head())
# head 메서드는 데이터프레임에서 가장 앞에 있는 5개의 행을 출력


# In[9]:


import pandas as pd
# pandas를 pd로 줄여서 사용


# In[10]:


print(type(df))
# type 메서드는 파이썬 내장 메서드
# 자료형을 출력


# In[11]:


print(df.shape)
# 1번째 값 : 행의 크기, 2번째 값 : 열의 크기


# In[12]:


print(df.columns)
# 데이터프레임의 열 이름 확인


# In[13]:


print(df.dtypes)


# In[15]:


print(df.info())
# 걊의 자료형은 dtypes 속성이나 info 메서드로 쉽게 확인 가능


# In[16]:


# object - string - 문자열
# int64 - int - 정수
# float64 - float - 소수점을 가진 숫자
# datetime64 - datetime - 파이썬 표준 라이브러리인 datetime이 반환하는 자료형


# In[17]:


country_df = df['country']


# In[18]:


print(type(country_df))
# country_df 에 저장된 데이터의 자료형이 시리즈라는 것을 확인 가능


# In[23]:


print(country_df.head())
print(country_df.tail())
# head는 상위 5개 데이터, tail은 하위 5개 데이터 출력


# In[26]:


subset = df[['country','continent','year']]
print(type(subset))
# 리스트에 열 이름을 전달하면 여러 개의 열을 한 번에 추출할 수 있다
# country, continent, year인 열을 추출하여 변수 subset에 저장한 것, 2개 이상의 열을 추출하였으므로 시리즈 X, 데이터프레임 O


# In[27]:


print(subset.head())
print(subset.tail())


# In[28]:


# 행 단위 데이터 추출하기
# loc : 인덱스를 기준으로 행 데이터 추출
# iloc : 행 번호를 기준으로 행 데이터 추출


# In[30]:


print(df.head())


# In[31]:


print(df.loc[0])
# 인덱스가 0인 행 데이터를 추출한 것, -1과 같이 인덱스에 없는 값을 사용하면 오류 발생


# In[32]:


print(df.loc[99])
# 인덱스가 99인 행 데이터를 추출한 것


# In[33]:


print(df.loc[-1])
# -1은 인덱스에 없는 값. 오류 발생


# In[36]:


number_of_rows = df.shape[0]
last_row_index = number_of_rows - 1
print(df.loc[last_row_index])

# 데이터프레임(df)의 마지막 행 데이터 추출.
# shape[0]에 행 크기 (1704)가 저장되어 있다는 점을 이용, 마지막 행의 인덱스 값을 구함
# shape[0] - 1 을 뺸 값으로 실제 마지막 행인 1703 행 데이터를 추출한 것이다. 
# 1을 뺀 이유는 index 값이 0부터 시작하기 때문


# In[37]:


print(df.tail(n=1))
# 데이터프레임의 마지막 행 데이터를 추출하는 또 다른 방법
# tail 메서드를 사용
# tail 메서드의 인자 n에 1을 전달하면 마지막 1행의 데이터를 추출할 수 있음


# In[38]:


print(df.tail(n=2))
# tail 메서드 인자 2를 대입할 시 마지막 2개의 행의 데이터를 추출할 수 있다.


# In[41]:


print(df.loc[[0, 99, 999]])
# 인덱스가 0, 99, 999인 데이터를 한 번에 추출하고 싶을 때는 리스트에 원하는 인덱스를 담아 loc 속성에 전달


# In[42]:


subset_loc = df.loc[0]
subset_tail = df.tail(n=1)


# In[43]:


print(type(subset_loc))
print(type(subset_tail))
# loc 속성이 반환한 데이터 자료형은 시리즈이고 tail 메서드가 반환한 데이터 자료형은 데이터프레임이다.


# In[47]:


print(df.iloc[1])
print(df.iloc[99])
# loc 속성은 df의 인덱스를 사용하여 데이터를 추출했지만, iloc 속성은 데이터 순서를 의미하는 행 번호를 사용하여 데이터를 추출한다.
# 지금은 인덱스와 행 번호가 동일하여 동일한 결괏값이 출력됩니다.


# In[48]:


print(df.iloc[-1])
print(df.iloc[1710])
# -1을 전달하여 마지막 행 데이터를 추출한 것. 하지만 df에 아예 존재하지 않는 행 번호를 전달하면 오류가 발생한다.


# In[49]:


print(df.iloc[[0,99,999]])
# iloc 속성도 여러 데이터를 한 번에 추출할 수 있다. loc 속성을 사용했던 것처럼 원하는 데이터의 행 번호를 리스트에 담아 전달한다.


# In[50]:


subset = df.loc[:, ['year', 'pop']]
print(subset.head())
# 모든 행 (:) 의 데이터에 대해 year, pop 열을 추출하는 방법
# loc 속성의 열 지정값에 정수 리스트를 전달하면 오류가 발생하니 주의!


# In[52]:


subset = df.iloc[:, [2, 4, -1]]
print(subset.head())
# iloc 속성의 열 지정값에 문자열 리스트를 전달하면 오류 발생! 정수로 전달할 것.


# In[53]:


small_range = list(range(5))


# In[54]:


print(small_range)


# In[58]:


print(type(small_range))


# In[59]:


subset = df.iloc[:, small_range]
print(subset.head())
# small_range 값이 [0,1,2,3,4]. 따라서 열 지정값에 따른 데이터를 추출하였다.
# iloc 속성의 열 지정값에는 정수 리스트를 전달해야만 한다!


# In[60]:


small_range = list(range(3,6))
print(small_range)
# 3~5 범위의 정수 리스트를 구하려면 list(range(3,6))이라고 입력하면 된다.


# In[61]:


subset = df.iloc[:, small_range]
print(subset.head())
# range(3,6)이 반환한 제너레이터를 정수값을 가진 리스트 [3,4,5]로 변환하여
# iloc의 열 지정값에 전달해서 3,4,5열을 가져왔다.


# In[62]:


small_range = list(range(0,6,2))
subset = df.iloc[:, small_range]
print(subset.head())
# range 메서드에 range(0,6,2)와 같은 방법으로 3개의 인자를 전달하면
# 0부터 5까지 2만큼 건너뛰는 제너레이터를 생성한다.
# 즉, 0~5 중 0, 2, 4 로 이루어진 정수 리스트를 얻을 수 있다.


# In[64]:


subset = df.iloc[:, :3]
print(subset.head())
# 실무에선 range 메서드보다는 간편하게 사용할 수 있는 파이썬 슬라이싱 구문을 더 선호한다.
# range 메서드가 반환한 제너레이터를 리스트로 변환하는 등의 과정을 거치지 않아도 되기 때문
# list(range(3))과 [:3]의 결괏값은 동일하다
# [0,1,2]


# In[65]:


subset = df.iloc[:, 0:6:2]
print(subset.head())
# 슬라이싱 구문


# In[66]:


print(df.iloc[[0,99,999],[0,3,5]])
# iloc 속성으로 0,99,999번째 행의 0,3,5번째 열 데이터를 추출하였다.


# In[67]:


print(df.loc[[0,99,999],['country','lifeExp','gdpPercap']])
# iloc 속성의 열 지정값으로 정수 리스트를 전달하는 것이 간편할 수 있다.
# 다만, 이렇게 작성된 코드의 경우 나중에 어떤 데이터를 추출하기 위한 코드인지 파악이 어려울 수 있다.
# 그래서 보통은 loc 속성을 이용하여 열 지정값으로 열 이름을 전달하는 방법을 이용한다.


# In[68]:


print(df.loc[10:13, ['country','lifeExp','gdpPercap']])
# 인덱스가 10인 행부터 13인 행의 country, lifeExp, gdpPercap 열 데이터를 추출하는 코드이다.


# In[69]:


print(df.head(n=10))
# 데이터 집합에서 0~9번째 데이터를 추출하여 출력한 것


# In[70]:


# 1. lifeExp 열을 연도별로 그룹화하여 평균 계산하기
print(df.groupby('year')['lifeExp'].mean())
# 데이터프레임의 groupby 메서드에 year 열을 전달하여 연도별로 그룹화한 다음 lifeExp 열을 지정하여 mean 메서드로 평균을 구한 것


# In[72]:


grouped_year_df = df.groupby('year')
print(type(grouped_year_df))
# groupby 메서드에 year 열 이름을 전달하면 연도별로 그룹화한 country, ... , gdpPercap 열을 모은 df를 얻을 수 있다.


# In[73]:


print(grouped_year_df)
# 뒤의 메모리 주소는 실행 환경에 따라 다르게 출력됩니다.


# In[74]:


grouped_year_df_lifeExp = grouped_year_df['lifeExp']
print(type(grouped_year_df_lifeExp))
# lifeExp 열을 추출한 결과.
# 그룹화한 시리즈를 얻을 수 있음. 즉, 연도별로 그룹화 된 lifeExp 열을 얻을 수 있다.


# In[75]:


mean_lifeExp_by_year = grouped_year_df_lifeExp.mean()
print(mean_lifeExp_by_year)
# 연도별로 그룹화한 lifeExp에 mean 메서드를 사용했기 때문에 각 연도별 lifeExp 열의 평균값을 얻을 수 있다.


# In[76]:


multi_group_var = df.groupby(['year','continent',])[['lifeExp','gdpPercap']].mean()
print(multi_group_var)
# year, continent 열로 그룹화한 그룹 데이터프레임에서 lifeExp, gdpPercap 열만 추출하여 평균값을 구한 것


# In[77]:


print(type(multi_group_var))


# In[78]:


print(df.groupby('continent')['country'].nunique())
# 그룹화한 데이터의 개수가 몇 개인지 확인
# 빈도 수 : nunique 메서드 사용
# continent를 기준으로 df를 만들고 country 열만 추출하여 데이터의 빈도 수를 계산하였다.


# In[80]:


get_ipython().run_line_magic('matplotlib', 'inline')
import matplotlib.pyplot as plt


# In[81]:


global_yearly_life_expectancy = df.groupby('year')['lifeExp'].mean()
print(global_yearly_life_expectancy)
# year 열을 기준으로 lifeExp 열만 추출하여 평균값을 구함


# In[82]:


global_yearly_life_expectancy.plot()
# 구한 값에 plot 메서드를 사용하면 그래프가 만들어짐
# 시간에 따른 평균 생명 예측치를 보여주는 판다스 기본 그래프


# In[ ]:




