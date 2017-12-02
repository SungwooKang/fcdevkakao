# -*- coding: utf-8 -*- 

from django.db import models
import datetime
import requests
from bs4 import BeautifulSoup as bs

# Create your models here.
def lotto():
    # now = datetime.datetime.now()
    # nh = datetime.time()
    # lh = datetime.time(20,50)

    # day = datetime.datetime.today().weekday()

    response = requests.get('http://www.nlotto.co.kr/gameResult.do?method=byWin')
    result = bs(response.text, 'html.parser')
    numbers = [tag['alt'] for tag in result.select('.contentsArticle p.number img')]
    count = result.find("h3",{"class":"result_title"}).text.split('\n')
    c1 = count[2]
    c2 = c1[1:-1]
    print(c2)
    print("제 {0} 회차 로또 당첨 번호는 {1}, {2}, {3}, {4}, {5}, {6} 이며, 2등 당첨 번호는 {7} 입니다.".format(count[0], numbers[0], numbers[1], numbers[2], numbers[3], numbers[4], numbers[5], numbers[6]))
