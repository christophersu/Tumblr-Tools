# quick-post.py
# Christopher Su
# http://christophersu.net/
## Asks for an image URL, quickly queues a photo post to Tumblr with it as the source and tags.

import pytumblr
import OAuthCredentials
import pickle

def main():
	already_posted = pickle.load(open("quick-queue_save.txt", "rb"))

	client = pytumblr.TumblrRestClient(OAuthCredentials.TUMBLR_CONSUMER_KEY, OAuthCredentials.TUMBLR_CONSUMER_SECRET, OAuthCredentials.TUMBLR_OAUTH_TOKEN, OAuthCredentials.TUMBLR_OAUTH_TOKEN_SECRET)
	blogName = 'BLOG NAME'
	tagArray = ['COMMA SEPARATED TAGS']

	while True:
		source_url = raw_input("Enter an image URL: ")
		if source_url == 'exit':
			break
		elif source_url not in already_posted:
			client.create_photo(blogName, state='queue', source=source_url, tags=tagArray)
			already_posted.append(source_url)
			pickle.dump(already_posted, open("quick-queue_save.txt", "wb"))
			print "Added.\n"
		else:
			print "You've posted this image before.\n"

if __name__ == '__main__':
    main()