from email.parser import Parser
fileread="enron_mail_20150507.tar\\maildir\\saibi-e\\all_documents\\1_"
with open(fileread,"r") as f:
	data=f.read()
	
email=Parser().parsestr(data)

print("\nTo: ",email['to'])
print("\nFrom: ",email['from'])
print("\nSubject: ",email['subject'])
print("\nBody: ",email.get_payload())