from selenium import webdriver
from time import sleep
import json

with open('.\data.json', encoding='utf-8') as s:
    data = json.loads(s.read())

timeInput = input('Enter time in second(s): ')

b = webdriver.Ie('.\\IEDriverServer.exe')

while True:
    b.maximize_window()
    for site in data['sites']:
        
        b.get(site)
        sleep(int(timeInput))
