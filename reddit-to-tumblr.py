#!/usr/bin/env python
'''
reddit-to-tumblr.py
Christopher Su
http://christophersu.net/
Gets images from a subreddit and posts them to Tumblr.
'''

import mimetypes, urllib2, pickle, logging, os
from time import gmtime, strftime
from random import randrange
import pytumblr
import praw
import OAuthCredentials

def main():
	## Configuration
	blogName = 'BLOG NAME'
	# postStatus = 'published' # publish posts directly
	postStatus = 'queue' # send new posts to queue

	## Logging setup
	dir = os.path.dirname(__file__)
	LOG_FILENAME = os.path.join(dir, 'reddit-to-tumblr.log')
	logging.basicConfig(filename=LOG_FILENAME,level=logging.DEBUG)
	logging.debug("Activated: " + strftime("%Y-%m-%d %H:%M:%S", gmtime()))

	save_array = pickle.load(open(os.path.join(dir, 'reddit-to-tumblr_save.txt'), "rb"))

	r = praw.Reddit(user_agent='Subot 1.0')

	if (randrange(1,3) == 1): # generate a random number between 1 and 2
		subredditToUse = 'SUBREDDIT NAME'
	else:
		subredditToUse = 'SUBREDDIT NAME'

	### Use submissions from hot/top
	submissions = r.get_subreddit(subredditToUse).get_top_from_day(limit=10)
	submission = next(submissions)

	### Use a random submission
	#submission = r.get_random_submission(subredditToUse)
	
	source_url = submission.url
	while (submission.id in save_array) or (submission.is_self) or not (is_image_and_ready(source_url)):
		submission = next(submissions) # if using top/hot submission
		#submission = r.get_random_submission('SUBREDDIT NAME') # if using random submission
		source_url = submission.url

	client = pytumblr.TumblrRestClient(OAuthCredentials.TUMBLR_CONSUMER_KEY, OAuthCredentials.TUMBLR_CONSUMER_SECRET, OAuthCredentials.TUMBLR_OAUTH_TOKEN, OAuthCredentials.TUMBLR_OAUTH_TOKEN_SECRET)
	if subredditToUse == 'SUBREDDIT NAME':
		tagArray = ['COMMA SEPARATED TAGS']
	else:
		tagArray = ['COMMA SEPARATED TAGS']

	logging.debug(client.create_photo(blogName, state=postStatus, source=source_url, tags=tagArray)) # make the post and log
	logging.debug("blogName: %s, subredditToUse: %s, postStatus: %s, submission.id: %s" % (blogName, subredditToUse, postStatus, submission.id))

	save_array.append(submission.id)
	pickle.dump(save_array, open(os.path.join(dir, 'reddit-to-tumblr_save.txt'), "wb"))

def is_url_image(url):    
    mimetype,encoding = mimetypes.guess_type(url)
    return (mimetype and mimetype.startswith('image'))

def check_url(url):
    try:
        headers={
            "Range": "bytes=0-10",
            "User-Agent": "Subot 1.0",
            "Accept":"*/*"
        }

        req = urllib2.Request(url, headers=headers)
        response = urllib2.urlopen(req)
        return response.code in range(200, 209)
    except Exception, ex:
        return False

def is_image_and_ready(url):
	# if ("imgur.com" in url) and not (url.endswith(".jpg") or url.endswith(".jpg")): url += ".jpg" # if the link goes to an imgur page and not directly to the image, then append .jpg
    return is_url_image(url) and check_url(url)

if __name__ == '__main__':
    main()