# coding=utf-8
import requests
from bs4 import BeautifulSoup

'''
requests不是Python的标准库。

Python requests 是一个常用的 HTTP 请求库，可以方便地向网站发送 HTTP 请求，并获取响应结果。
requests 模块比 urllib 模块更简洁。

'''

'''
BeautifulSoup

Beautiful Soup is a library that makes it easy to scrape information from web pages. It sits atop an HTML or XML parser, providing Pythonic idioms for iterating, searching, and modifying the parse tree.
https://pypi.org/project/beautifulsoup4/

'''

url = "https://www.msn.cn/zh-cn/weather/forecast/in-%E5%B9%BF%E4%B8%9C%E7%9C%81,%E5%B9%BF%E5%B7%9E%E5%B8%82"
headers = {
    "Accept": "*/*",
    'user-agent': 'dddd',
    'Referer': 'https://www.tianqi.com/',
    'Sec-Ch-Ua': 'Google Chrome";v="123", "Not:A-Brand";v="8", "Chromium";v="123',
    'Sec-Ch-Ua-Mobile': '?0',
    'Sec-Ch-Ua-Platform': 'Windows'
    }
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')
print(soup.prettify())
temperture = soup.find(class_='summaryTemperatureCompact-E1_1 summaryTemperatureHover-E1_1').text.strip()
# temperture2 = soup.find(class_='labelUpdatetime-DS-EntryPoint1-1').text.strip()
location = soup.find(id='WeatherOverviewLocationName').text.strip()
description = soup.find(id='CurrentWeatherFeedback').text.strip()
CurrentWeatherSummary = soup.find(id='CurrentWeatherSummary').text.strip()
print("地区 %s" % location)
print("气温 %s" % temperture)
# print("气温 %s" % temperture2)
print("天气 %s" % description)
print("概述 %s" % CurrentWeatherSummary)

