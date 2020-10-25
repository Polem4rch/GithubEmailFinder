import requests, json

username = input("add username: ")
url = "https://api.github.com/users/%s/events/public" % username


response = requests.get(url)
result = json.loads(response.content.decode('utf-8'))

user_list = []

for r in result:
	for k,v in iter(r.items()):
		if k == 'actor':
			if v not in user_list:
				user_list.append(v)

print()
for u in user_list:
	for k,v in u.items():
		print('%s: %s'%(k.upper(),v))
	print()

if not user_list:
	print('error: user not found')