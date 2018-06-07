import os 

rootdir="enron_mail_20150507.tar\\maildir\\saibi-e"

for directory, subdirectory, filename in os.walk(rootdir):
	print(directory,subdirectory,len(filename))