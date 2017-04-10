import praw
import sys
import os, shutil
from bs4 import BeautifulSoup
import requests
import re


def save_img(url):
	#Once we have decided that the URL is an image, write to file
	def write_to_img(r):
		if r.status_code == 200:
			with open('./pics/' + url[-8:], 'wb') as file:
				r.raw.decode_content = True
				shutil.copyfileobj(r.raw, file)
			return True
		else:
			return False

	r = requests.get(url, stream=True)
	if re.search('(http://i.imgur.com/(?!a))(?!.*)', url):
		#Links to an imgur page containing a link to the image
		soup = BeautifulSoup(r.content, 'html.parser')

		image_src = soup.find(itemprop="contentURL").get('src')
		request = "(http://i.imgur.com/" + image_src
		r = requests.get(request, stream=True)
		return write_to_img(r)

	elif re.findall('(http://i.imgur.com/(.*))(\?.*)?', url):
		#Links to an imgur page that is the image source
		return write_to_img(r)

	elif re.search('(https://i.redd.tr/(.*))(\?.*)?', url):
		#Links to Reddit image host
		request = re.findall('(https://i.redd.tr/(.*))(\?.*)?', url)
		return write_to_img(r)

	return False

def get_pics(subreddit):
	i = 1
	for post in subreddit.top(limit = 10):
		if i > 3:
			break
		if save_img(post.url):
			i += 1


def find_top_three_pics():
	#Removes current photos in pics subdirectory
	for file in os.listdir('./pics'):
		os.unlink('./pics/' + file)

	#Creates subreddit instances with PRAW
	spaceporn = reddit.subreddit('SpacePorn')
	earthporn = reddit.subreddit('EarthPorn')
	pic = reddit.subreddit('Pic')


	#Stupid lack of case in Python!
	try:
		if sys.argv[1] == 'SPE':
			#Get pics from /r/SpacePorn, /r/Pic, /r/EarthPorn
			get_pics(spaceporn)
			get_pics(earthporn)
			get_pics(pic)

		elif sys.argv[1] == 'SP':
			#Get pics from /r/SpacePorn, /r/Pic
			get_pics(spaceporn)
			get_pics(pic)

		elif sys.argv[1] == 'SE':
			#Get pics from /r/SpacePorn, /r/EarthPorn
			get_pics(spaceporn)
			get_pics(earthporn)
		elif sys.argv[1] == 'EP':
			#Get pics from /r/EarthPorn, /r/Pic
			get_pics(earthporn)
			get_pics(pic)

		elif sys.argv[1] == 'P':
			#Get pics from /r/Pic
			get_pics(pic)
		elif sys.argv[1] == 'E':
			#Get pics from /r/EarthPorn
			get_pics(earthporn)
		elif sys.argv[1] == 'S':
			#Get pics from /r/SpacePorn
			get_pics(pic)
		else:
			print("Argument not recognized.")
			sys.exit(1)
	except IndexError:
		print("Argument not found.")
		sys.exit(1)



if __name__ == "__main__":
	reddit = praw.Reddit(client_id='JhNp1qEt7aeMRQ', client_secret=None, redirect_uri='http://localhost:8080', user_agent='Ubuntu Background Scraper by Isaac Samuel')

	find_top_three_pics()

	#Set pic, set timer, run continously