# importing modules
import requests
from bs4 import BeautifulSoup
import pandas as pd 
# URL for scrapping data
url = 'https://www.worldometers.info/coronavirus/countries-where-coronavirus-has-spread/'
 
# get URL html
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')

data= soup.find_all('td')


count =0
a=int(len(data)/4)
country=[]
cases =[]
death=[]
region=[]

for x in range (a) : 
    
    country.append(data[count].string)
    count+=1
    cases.append(data[count].string)
    count+=1
    death.append(data[count].string)
    count+=1
    region.append(data[count].string)
    count+=1
Cases =[]
Death=[]

for x in cases: 
    a=x 
    b=int(a.replace(',',''))
    Cases.append(b)


for x in death:
    a=x
    b=int(a.replace(',',''))
    Death.append(b)



df = pd.DataFrame (country, columns = ['Country'])
df1 = pd.DataFrame (Cases)
df2 = pd.DataFrame (Death)
df3 = pd.DataFrame (region)

df['Cases']=df1
df['Death']=df2
df['Region']=df3

print (df)

print (df.describe())

print (df.info())