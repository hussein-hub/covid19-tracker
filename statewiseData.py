# import requests
# import json
# import matplotlib.pyplot as plt
# def giveGraph(n):
#     dates = []
#     cases = []
#
#     url = "https://api.covid19india.org/data.json"
#     page = requests.get(url)
#     data = json.loads(page.text)
#     for i in range(-1, (-1) * (n + 1), -1):
#         dates.append(data["cases_time_series"][i]["date"][:-4])
#         cases.append(int(data["cases_time_series"][i]["dailydeceased"]))
#         # cases.append(int(data["cases_time_series"][i]["dailyconfirmed"]))
#
#     dates.reverse()
#     cases.reverse()
#     # print(dates)
#     # print(cases)
#     plt.figure(figsize=(8, 8))
#     plt.plot(dates, cases, marker='o')
#     plt.xlabel('Date')
#     plt.xticks(rotation=35)
#     plt.ylabel('Number of Cases')
#     plt.show()
#
# giveGraph(12)

import datetime

date_time_str = '08/11/21'
date_time_obj = datetime.datetime.strptime(date_time_str, '%d/%m/%y')

print('Date:', date_time_obj.date())