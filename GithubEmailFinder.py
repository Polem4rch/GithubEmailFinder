import requests, json


username = input("add username: ")
url = "https://api.github.com/users/%s/events/public" % username

response = requests.get(url)

data = json.loads(response.content.decode('utf-8'))[0]['payload']['commits'][0]['author']['email']
print(data)