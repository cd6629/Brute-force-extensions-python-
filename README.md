# Python-scripts
Random Python scripts

# EDB-ID-44595-Wordpress-Python-Privesc-Script

I wrote this small script as an alternative to a Metasploit Wordpress privilege escalation module (44595.rb), for the TryHackMe room Jack. The only issue was formatting the cookie properly for the second request. The initial request responds with three separate cookies, one for the test, one for plugins and one for the admin page. Inspecting the headers reveal that the admin page is the last cookie and I was able split accordingly. 

Proof showing the 200 OK status code:


![Alt text](https://gblobscdn.gitbook.com/assets%2F-M8-SyxgckWEMfZfndbo%2F-MFiRLcHI0Wyu9VFcMnW%2F-MFiTscogS5IujitfADf%2Fimage.png?alt=media&token=d78cbe03-9251-4e5b-98c0-7426e6f0ad7b)
