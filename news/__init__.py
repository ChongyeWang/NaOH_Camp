from django.shortcuts import render

# Create your views here.
from celery.task.schedules import crontab
from celery.decorators import periodic_task
from celery.utils.log import get_task_logger

import requests
import time
from bs4 import BeautifulSoup
from urllib.request import urlopen

import re
from datetime import datetime



logger = get_task_logger(__name__)


@periodic_task(
    run_every=(crontab()),
    name="scratch_news",
    ignore_result=True
)
def scratch_news():
	"""
	Scratch news
	"""
	all_news = []

	#EA
	try:
		ea = []
		url = 'https://www.ea.com/games/command-and-conquer/command-and-conquer-remastered/news?isLocalized=true'

		response = requests.get(url)

		soup = BeautifulSoup(response.text, "html.parser")

		list = soup.find("body")

		ea_tile = list.find_all('ea-tile')

		ea_date = []
		ea_title = []
		ea_link = []

		for ea in ea_tile:
		    # print(ea['eyebrow-text'])
		    # print(ea['title-text'])
		    ea_title.append(ea['title-text'])
		    ea_date.append(ea['eyebrow-text'])

		ea_cta = list.find_all('ea-cta')
		for ea in ea_cta:
		    link = 'https://www.ea.com' + ea['link-url']
		    # print(link)
		    ea_link.append(link)

		for i in range(len(ea_title)):
			all_news.append((ea_title[i], ea_link[i], ea_date[i]))

	except:
		pass


	#rz
	try:
		rz_date = []
		rz_title = []
		rz_link = []


		url2 = 'http://www.hongjing3.com/zixun/'


		res = requests.get(url2)
		res.encoding = 'gb18030'
		soup = BeautifulSoup(res.text,'lxml')

		list = soup.find("div", {"class":"left_3"})


		for link in list.find_all('a', {"class":"t"}):
		    # print(link.getText())
		    # print(link['href'])
		    rz_title.append(link.getText())
		    rz_link.append(link['href'])


		for date in list.find_all('em'):
		    try:
		        match = re.search(r'\d{4}-\d{2}-\d{2}', date.getText())
		        get_date = datetime.strptime(match.group(), '%Y-%m-%d').date()
		        # print(get_date.strftime('%Y-%m-%d'))
		        rz_date.append(get_date.strftime('%Y-%m-%d'))
		    except:
		        rz_date.append('N/A')

	# print(rz_date)


		for i in range(len(rz_title)):
			all_news.append((rz_title[i], rz_link[i], rz_date[i]))

	except:
		pass


	#moddb


	try:
		moddb_title = []
		moddb_link = []
		moddb_date = []

		url3 = 'https://www.moddb.com/games/cc-red-alert-2/mods'

		response = requests.get(url3)

		soup = BeautifulSoup(response.text, "html.parser")

		list = soup.find_all(class_=re.compile("^row rowcontent"))[:5]

		for ele in list:
		    link = ele.find('a')
		    moddb_link.append('https://www.moddb.com' + link['href'])
		    moddb_title.append(link['title'])
		    moddb_date.append(ele.find('time').getText())


		for i in range(len(moddb_title)):
			all_news.append((moddb_title[i], moddb_link[i], moddb_date[i]))

	except:
		pass


	from .models import News

	News.objects.all().delete()

	for i in range(len(all_news)):
		news_object = News(title=all_news[i][0], link=all_news[i][1], date=all_news[i][2])
		news_object.save()
    
