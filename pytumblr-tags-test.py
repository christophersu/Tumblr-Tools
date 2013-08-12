def main():
	params = {'tags': ['omg', 'nice']}
	# params['tags'] = ",".join(params['tag']s'])
	# params['tags'] = ', '.join([x.strip() for x in params['tags'].split(',')])
	params['tags'] = ', '.join([i.split(',') for i in params['tags']])
	print params['tags']

if __name__ == '__main__':
    main()