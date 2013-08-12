from tumblpy import *
import OAuthCredentials
import pickle

def main():
	final_oauth = pickle.load(open("tumblr_oauth_tokens.txt", "rb"))
	OAUTH_TOKEN = final_oauth[0]
	OAUTH_TOKEN_SECRET = final_oauth[1]

	t = Tumblpy(OAuthCredentials.TUMBLR_CONSUMER_KEY, OAuthCredentials.TUMBLR_CONSUMER_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)

	blog_url = t.post('user/info')
	blog_url = blog_url['user']['blogs'][0]['url']
	print blog_url

	try:
	    post = t.post('post', blog_url=blog_url, params={'type':'photo', 'caption': 'Test Caption', 'data': photo})
	    print post
	except TumblpyError, e:
	    # Maybe the file was invalid?
	    print e.message

if __name__ == '__main__':
    main()