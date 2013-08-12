import pytumblr
import OAuthCredentials

def main():
	client = pytumblr.TumblrRestClient(OAuthCredentials.a, OAuthCredentials.b, OAuthCredentials.c, OAuthCredentials.d)
	blogName = 'BLOG_NAME'
	client.create_photo(blogName, source='LINK TO AN IMAGE', tags=['PUT SOME TAGS IN A STRING ARRAY HERE'])

if __name__ == '__main__':
    main()