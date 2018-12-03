from selenium import webdriver
from time import sleep
import json

with open('.\data.json', encoding='utf-8') as s:
    data = json.loads(s.read())

# urls = []

# again = True

timeInput = input('Enter time in second(s): ')

# while again:
#     x = input('Enter url:\n')
#     urls.append(x)

#     insert = input('Insert more urls? (y/n)')
#     if insert.lower() == 'y':
#         again = True
#     elif insert.lower() == 'n':
#         again = False

# print(urls)

b = webdriver.Chrome('.\chromedriver.exe')
# 'E:\Data\IEDrive\IEDriverServer.exe'('C:\chromedrive\geckodriver.exe')
while True:
    # for i, url in enumerate(urls):
    #     b.maximize_window()
    #     b.get(url)
    #     sleep(3)
    for site in data['sites']:
        b.maximize_window()
        b.get(site)
        sleep(int(timeInput))
