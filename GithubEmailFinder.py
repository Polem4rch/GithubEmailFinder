import requests


url1 = "https://api.github.com/users/"
url2 = input("add username: ")
url3 = "/events/public"
all = url1 + url2 + url3


response = requests.get(all)
print(response.json())
