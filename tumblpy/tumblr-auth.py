from tumblpy import *
import OAuthCredentials
import pickle

def main():
	t = Tumblpy(OAuthCredentials.TUMBLR_CONSUMER_KEY, OAuthCredentials.TUMBLR_CONSUMER_SECRET)

	auth_props = t.get_authentication_tokens(callback_url='localhost')
	auth_url = auth_props['auth_url']

	OAUTH_TOKEN_SECRET = auth_props['oauth_token_secret']

	print 'Connect with Tumblr via: %s' % auth_url

	OAUTH_TOKEN = raw_input('\nWhat is your OAUTH_TOKEN? ')
	oauth_verifier = raw_input('What is your oauth_verifier? ')

	t = Tumblpy(OAuthCredentials.TUMBLR_CONSUMER_KEY, OAuthCredentials.TUMBLR_CONSUMER_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)

	authorized_tokens = t.get_authorized_tokens(oauth_verifier)

	final_oauth_token = authorized_tokens['oauth_token']
	final_oauth_token_secret = authorized_tokens['oauth_token_secret']

	final_oauth = [final_oauth_token, final_oauth_token_secret]

	pickle.dump(final_oauth, open("tumblr_oauth_tokens.txt", "wb"))

if __name__ == '__main__':
    main()