import os
from email.parser import Parser
from collections import Counter

folder="enron_mail_20150507.tar\\maildir\\saibi-e\\all_documents"
def anlaysemail(inputfile,write_to,write_from,write_body):
	with open(inputfile,"r") as f:
		data=f.read()
		email=Parser().parsestr(data)
	
	if email['to']:
		email_to=email['to']
		email_to=email_to.replace("\n","")
		email_to=email_to.replace("\t","")
		email_to=email_to.replace(" ","")
		email_to=email_to.split(",")
		
		
		for email_to_1 in email_to:
			write_to.append(email_to_1)
		
	write_from.append(email['from'])
	write_body.append(email.get_payload())
	
write_to=[]
write_from=[]
write_body=[]

for directory,subdirectory,filenames in os.walk(folder):
	for filename in filenames:
		anlaysemail(os.path.join(directory,filename),write_to,write_from,write_body)
		
with open("EMAIL_to.txt","w") as f:
	print("Most Common Reciever: ",Counter(write_to).most_common(1))
	for write_t in write_to:
		if write_t:
			f.write(write_t)
			f.write("\n")

with open("EMAIL_from.txt","w") as f:
	print("Most Common Sender: ",Counter(write_from).most_common(1))
	for write_f in write_from:
		if write_f:
			f.write(write_f)
			f.write("\n")
	
with open("EMAIL_body.txt","w") as f:
	for write_b in write_body:
		print(Counter(write_b.split(" ")).most_common(1))
		if write_b:
			f.write(write_b)
			f.write("\n")