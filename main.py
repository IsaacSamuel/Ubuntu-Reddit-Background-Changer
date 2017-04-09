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
		request = "http://i.imgur.com/" + image_src

	else if re.findall('http://i.imgur.com/(.*))(\?.*)?', url):
		#Links to an imgur page that is the image source
		request = re.findall('http://i.imgur.com/(.*))(\?.*)?', url)

	else if re.search('http://i.redd.tr/(.*))(\?.*)?', url):
		#Links to Reddit image host
		request = re.findall('http://i.redd.tr/(.*))(\?.*)?', url)

	if request:
		r = requests.get(request)
		#Write image to a file
		if r.status_code == 200:
			with open('./pics/' + str(count), 'wb') as file:
				r.raw.decode_content = True
				shutil.copyfileobj(r.raw, f)
			return True

	return False

def get_pics(subreddit)
	i = 1
	for post in subreddit.top(limit = 10):
		if i > 3:
			break
		if save_image(post.url):
			i += 1
			count += 1



def find_top_three_pics():
	count = 0
	#Removes current photos in pics subdirectory
	for file in os.listdir('./pics'):
		os.unlink('./pics' + file)

	spaceporn = reddit.subreddit('SpacePorn')
	earthporn = reddit.subreddit('SpacePorn')
	pic = earthporn = reddit.subreddit('SpacePorn')

	if args[1] == 'SPE':
		#Get pics from /r/SpacePorn, /r/Pic, /r/EarthPorn
		get_pics(spaceporn)
		get_pics(earthporn)
		get_pics(pic)

	else if args[1] == 'SP':
		#Get pics from /r/SpacePorn, /r/Pic
		get_pics(spaceporn)
		get_pics(pic)

	else if args[1] == 'SE':
		#Get pics from /r/SpacePorn, /r/EarthPorn
		get_pics(spaceporn)
		get_pics(earthporn)
	else if args[1] == 'EP':
		#Get pics from /r/EarthPorn, /r/Pic
		get_pics(earthporn)
		get_pics(pic)

	else if args[1] == 'P':
		#Get pics from /r/Pic
		get_pics(pic)
	else if args[1] == 'E':
		#Get pics from /r/EarthPorn
		get_pics(earthporn)
	else if args[1] == 'S':
		#Get pics from /r/SpacePorn
		get_pics(pic)
	else:
		Print("Some problem with the keywords")
		System.exit(1)



if __name__ == "__main__":
	reddit = praw.Reddit(client_id='JhNp1qEt7aeMRQ', client_secret=None, redirect_uri='http://localhost:8080', user_agent='Ubuntu Background Scraper by Isaac Samuel')

	find_top_three_pics()

	#Set pic, set timer, run continously