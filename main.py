import requests 
import random
letters = "qwertyuioplkjhgfdsazxcvbnmQWERTYUIOPLKJHGFDSAZXCVBNM123456789"

username = input("Email/Username: ")
password = input("Password: ")
req = requests.session()
accesheaders = {
    "Authorization": "Basic M25WdVNvQlpueDZVNHZ6VXhmNXc6QmNzNTlFRmJic2RGNlNsOU5nNzFzbWdTdFdFR3dYWEtTall2UFZ0N3F5cw=="
}
accespayload = {
    "grant_type": "client_credentials"
}
accesstokenreq = req.post("https://api.twitter.com/oauth2/token",data=accespayload,headers=accesheaders).json()
access_token = accesstokenreq["access_token"]
guestheaders = {
    "Authorization": "Bearer " + access_token
}
guesttokenreq = req.post("https://api.twitter.com/1.1/guest/activate.json",headers=guestheaders).json()
guest_token = guesttokenreq["guest_token"]

loginheaders = {
 "Authorization": f"Bearer {access_token}",
 "X-Guest-Token": guest_token,
 "User-Agent": "TwitterAndroid/8.19.0-release.01 (18190001-r-1) LGM-V300K/5.1.1 (LGE;LGM-V300K;Android;LGM-V300K;0;;1;2014)",
 "X-Twitter-Client-DeviceID": "".join(random.sample(letters,15)),
	"X-Twitter-Client-Language": "en-US",
	"X-Twitter-Client": "TwitterAndroid",
	"X-Twitter-API-Version": "5",
	"Optimize-Body": "true",
	"X-Twitter-Active-User": "yes",
	"X-Twitter-Client-Version": "8.19.0-release.01",
	"X-Guest-UUID": "".join(random.sample(letters,16)),
	"Accept": "application/json",
}
logindata = {
    "x_auth_identifier": username,
    "x_auth_password": password,
    "send_error_codes": "true",
    "x_auth_login_challenge": "1",
    "x_auth_country_code": "US"
}
loginrequest = req.post("https://api.twitter.com/auth/1/xauth_password.json",headers=loginheaders,data=logindata).json()
if "errors" in loginrequest:
    print("Not Working")
else: 
    print("Working !~")
