import praw
import sys
import os, shutil
from bs4 import BeautifulSoup
import requests
import re

def save_img(url):
	soup = BeautifulSoup(url)
	if re.search('(http://i.imgur.com/(?!a))(?!.*)', url):
		#Links to an imgur page containing a link to the image
		image_src = soup.find(itemprop="contentURL").get('src')
		#request = http://i.imgur.com/ + image_src
	else if re.findall('http://i.imgur.com/(.*))(\?.*)?', url):
		#Links to an imgur page that is the image source
	else if re.search('http://i.redd.tr/(.*))(\?.*)?', url):
		url = re.findall('http://i.redd.tr/(.*))(\?.*)?', url)


def find_top_three_pics():
	#Removes current photos in pics subdirectory
	for file in os.listdir('./pics'):
		os.unlink('./pics' + file)



	if args[1] == 'SPE':
		#Get pics from /r/SpacePorn, /r/Pic, /r/EarthPorn
		subreddit = reddit.subreddit('SpacePorn')
		i = 0
		for post in subreddit.top(limit = 10):
			if i > 2:
				break
			if save_image(post.url):
				i += 1




	else if args[1] == 'SP':
		#Get pics from /r/SpacePorn, /r/Pic
	else if args[1] == 'SE':
		#Get pics from /r/SpacePorn, /r/EarthPorn
	else if args[1] == 'EP':
		#Get pics from /r/EarthPorn, /r/Pic
	else if args[1] == 'P':
		#Get pics from /r/Pic
	else if args[1] == 'E':
		#Get pics from /r/EarthPorn
	else if args[1] == 'S':
		#Get pics from /r/SpacePorn
	else:
		Print("Some problem with the keywords")
		System.exit(1)



if __name__ == "__main__":
	reddit = praw.Reddit(client_id='JhNp1qEt7aeMRQ', client_secret=None, redirect_uri='http://localhost:8080', user_agent='Ubuntu Background Scraper by Isaac Samuel')

	find_top_three_pics()

	#Set pic, set timer, run continously