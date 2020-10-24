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


'''
{
   "id":"13842435482",
   "type":"MemberEvent",
   "actor":{
      "id":36511666,
      "login":"prykon",
      "display_login":"prykon",
      "gravatar_id":"",
      "url":"https://api.github.com/users/prykon",
      "avatar_url":"https://avatars.githubusercontent.com/u/36511666?"
   },
   "repo":{
      "id":302376363,
      "name":"prykon/condarco-bot",
      "url":"https://api.github.com/repos/prykon/condarco-bot"
   },
   "payload":{
      "member":{
         "login":"iruasi",
         "id":21202750,
         "node_id":"MDQ6VXNlcjIxMjAyNzUw",
         "avatar_url":"https://avatars2.githubusercontent.com/u/21202750?v=4",
         "gravatar_id":"",
         "url":"https://api.github.com/users/iruasi",
         "html_url":"https://github.com/iruasi",
         "followers_url":"https://api.github.com/users/iruasi/followers",
         "following_url":"https://api.github.com/users/iruasi/following{/other_user}",
         "gists_url":"https://api.github.com/users/iruasi/gists{/gist_id}",
         "starred_url":"https://api.github.com/users/iruasi/starred{/owner}{/repo}",
         "subscriptions_url":"https://api.github.com/users/iruasi/subscriptions",
         "organizations_url":"https://api.github.com/users/iruasi/orgs",
         "repos_url":"https://api.github.com/users/iruasi/repos",
         "events_url":"https://api.github.com/users/iruasi/events{/privacy}",
         "received_events_url":"https://api.github.com/users/iruasi/received_events",
         "type":"User",
         "site_admin":False
      },
      "action":"added"
   },
   "public":True,
   "created_at":"2020-10-14T12:24:27Z"
}
'''