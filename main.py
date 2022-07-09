#create this script ayto bruh
#edit and again work script by Tcxeh
from info import createpassword,chatlink,YourLink,key,app_name,nickname
from PIL import Image
#from keep_alive import keep_alive
#keep_alive()
import os
from bs4 import BeautifulSoup
from hmac import new
from  hashlib import sha1
import requests as req
from random import choice as ch
from time import sleep
import names
from colorama import Fore
from pyfiglet import figlet_format 
from secmail import SecMail as secmail
import aminofix
from aminofix import Client
from aminofix.lib.util.exceptions import ActionNotAllowed,TooManyRequests, IncorrectVerificationCode
import heroku3
def restart():
    heroku_conn = heroku3.from_key(key)
    botapp= heroku_conn.apps()[app_name]
    botapp.restart()
    

cid="151593687"    
char = 5
def geticon(client):
	urlx=client.get_all_users(size=100).profile.icon
	for url in urlx:
		if url is None or url=="None":
			pass
		else:
		  return url
		  break

def set_acc(email):
    client.login(email, password)
    url=geticon(client)
    try:
    	 client.edit_profile(icon=upload(url))
    except:
    	pass

def deviceId():
	identifier = os.urandom(20)
	return ("42" + identifier.hex() + new(bytes.fromhex("02B258C63559D8804321C5D5065AF320358D366F"), b"\x42" + identifier, sha1).hexdigest()).upper()

def log(cli: Client, email, password,device):
    try:
        cli.login(email, password)
        SID = f"{cli.sid}"
        with open("accounts.json", 'a') as x:
            acc = f'\n{{\n"email": "{email}",\n"password": "{password}",\n"deviceId": "{device}",\n"SID": "{SID}"\n}},'
            x.write(acc)
            print("Save Account !")
    except Exception as b:
        print(b)

send = open("accounts.json").read()


def box(email:str):
	try:
		sec = secmail()
		sleep(2.5)
		box = sec.get_messages(email)
		for message in box.id:
			msg = sec.read_message(email=email, id=message).htmlBody
			bs = BeautifulSoup(msg, 'html.parser')
			ims = bs.find_all('a')[0]
			link = (ims['href'])
			return link
	except:
		pass
no=int("5")
for _ in range(int(no)):
	password=createpassword
	os.remove("device.json")
	chose = "".join(ch("Tcxehkinguzair")for i in range(char))
	email = f"Tcxeh{chose}@wwjmp.com"
	device = deviceId()
	client =Client()
	try:
		nick="Tcxehbot"
		client.request_verify_code(email)
		verify_url = box(email)
		print(email)
		print(verify_url)
		data = {"url":verify_url}
		verify_code = req.post("https://captchasolver.neodouglas.repl.co/predict", data={"image": verify_url}).json()['captcha'][0]
		print(verify_code)
		client.register(nickname=nick, email=email, password=password, verificationCode=verify_code, deviceId=device)
		log(client, email, password, device)
		url=geticon(client)
		response=req.get(f"{url}")
		file=open("sam.png","wb")
		file.write(response.content)
		file.close()
		img=open("sam.png","rb")
		client.edit_profile(icon=img)
		client.join_community(cid)
		sub=aminofix.SubClient(comId=cid,profile=client.profile)
		private=client.get_from_code(YourLink).objectId
		chatId=client.get_from_code(chatlink).objectId
		sub.join_chat(chatId)
		snippetImage = "sam.png"
		with open(snippetImage, 'rb') as p:
			sub.send_message(chatId=chatId,message=f"""╭┉┉┅┄┄┈•◦ೋ•◦❥•◦ೋ

[BUC]Account Created Details
⦿ Nickname : {nick}
⦿ Online : ✅

[C]      •◦ೋ•◦❥•◦ೋ•┈┄┄┅┉┉╯
""",embedImage=p,embedContent=f"Click Image Check Account",embedLink=f"ndc://x{cid}/user-profile/",embedTitle=f"⦿ Profile Upload ✅")
		sub.start_chat(userId=private,message=send)
		print("Generator account Done.")
	except IncorrectVerificationCode:
		print("wrong code!")
		pass
	except ActionNotAllowed:
		input("Action Not Allowed!Change Vpn!")
		pass
	except TooManyRequests:
		input("Change Vpn To create more acconts:")
		pass
	else:
		input("change VPN:")
		pass
		


restart()
