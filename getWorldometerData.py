import requests
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt

country = input("Enter country name : ")

COUNTRY_URL = f"https://www.worldometers.info/coronavirus/country/{country}"
r = requests.get(COUNTRY_URL)

soup = BeautifulSoup(r.content, 'html.parser')
num = []
days = []
b = soup.findAll('button', attrs={'class': 'btn btn-light date-btn'})
d = soup.findAll('div', attrs={'class': 'newsdate_div'})
for i, j in zip(d, b):
    print(i.div.ul.li.strong.text + " : " + j.text)
    case = i.div.ul.li.strong.text.split(' ')
    case[0] = case[0].split(',')
    num.append(int(''.join(case[0])))
    days.append(j.text)
num.reverse()
days.reverse()
plt.figure(figsize=(8, 7))
plt.plot(days, num, marker='o', label='Case Trend')
plt.title('Last 5 Day Graph')
plt.xlabel('Date')
plt.ylabel('Number of Cases')
plt.legend()
plt.show()

#
# url = "https://worldometers.p.rapidapi.com/api/coronavirus/country/USA"
#
#
# headers = {
#     'x-rapidapi-key': "4de5bae009msh3d690447f433304p1d9fe1jsnf5600d22cfc9",
#     'x-rapidapi-host': "worldometers.p.rapidapi.com"
#     }
#
# response = requests.request("GET", url, headers=headers)
# data = response.json()
# print(data['data'])
