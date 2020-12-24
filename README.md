# Python-scripts
Random Python scripts

# CVE-2019-15107

I constructed this small script for the TryHackMe Room Source. Packet storm provided a base PoC script to build from including

- calling the payload via os.system with curl
- formatting the header with a referer 
- establishing a revere shell by downloading a bash script from an HTTP server

Proof showing the reverse shell on source:


![Alt text](https://gblobscdn.gitbook.com/assets%2F-M8-SyxgckWEMfZfndbo%2F-MPHWu1prkH4OkZauum6%2F-MPHaRpKZkcTqlOaPTD_%2FScreenshot%20from%202020-12-23%2021-31-58.png?alt=media&token=9c2163a2-e8c9-4a74-87f7-5cd877e0809b)


# EDB-ID-44595-Wordpress-Python-Privesc-Script

I wrote this small script as an alternative to a Metasploit Wordpress privilege escalation module (44595.rb), for the TryHackMe room Jack. The only issue was formatting the cookie properly for the second request. The initial request responds with three separate cookies, one for the test, one for plugins and one for the admin page. Inspecting the headers reveal that the admin page is the last cookie and I was able split accordingly. 

Proof showing the 200 OK status code:


![Alt text](https://gblobscdn.gitbook.com/assets%2F-M8-SyxgckWEMfZfndbo%2F-MFiRLcHI0Wyu9VFcMnW%2F-MFiTscogS5IujitfADf%2Fimage.png?alt=media&token=d78cbe03-9251-4e5b-98c0-7426e6f0ad7b)
