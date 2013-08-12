# quick-post.py
# Christopher Su
# http://christophersu.net/
## Asks for an image URL, quickly makes a photo post to Tumblr with it as the source and tags.

import pytumblr
import OAuthCredentials

def main():
	source_url = raw_input("Enter an image URL: ")
	client = pytumblr.TumblrRestClient(OAuthCredentials.TUMBLR_CONSUMER_KEY, OAuthCredentials.TUMBLR_CONSUMER_SECRET, OAuthCredentials.TUMBLR_OAUTH_TOKEN, OAuthCredentials.TUMBLR_OAUTH_TOKEN_SECRET)
	blogName = 'BLOG NAME'
	tagArray = ['COMMA SEPARATED TAGS']
	client.create_photo(blogName, source=source_url, tags=tagArray)
	print "done."

if __name__ == '__main__':
    main()