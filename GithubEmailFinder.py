import requests, json


username = input("add username: ")
url = "https://api.github.com/users/%s/events/public" % username

response = requests.get(url)

data = json.loads(response.content.decode('utf-8'))

for d in data:
	try:
		print(d['payload']['commits'][0]['author']['email'])
	except:
		pass