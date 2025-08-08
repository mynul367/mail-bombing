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