import os
import nltk.classify.util
from nltk.classify import NaiveBayesClassifier
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

rootdir="enron1.tar\\enron1"


def createdec(inputwords):
	mydict=[(words,True) for words in inputwords if words not in stopwords.words("English")]
	return mydict

spam_list=[]
ham_list=[]

for directory,subdirectory,filename in os.walk(rootdir):
	
	if(os.path.split(directory)[1]=="ham"):
		for files in filename: 
			with open(os.path.join(directory,files),"r",encoding="latin-1") as f:
				data=f.read()
				words=word_tokenize(data)
				intake=createdec(words)
				ham_list.append((intake,"ham"))
	
	if(os.path.split(directory)[1]=="spam"):
		for files in filename:
			with open(os.path.join(directory,files),"r",encoding="latin-1") as f:
				spam_list.append(f.read())
	
#print(spam_list[0])
#print(ham_list[2])
combined_list=spam_list+ham_list
random.shuffle(combine_list)

training_length=int(len(combined_set)*0.7)

training_set=combined_set[:training_length]
test_set=combined_set[training_length:]

classifier.NaiveBayesClassifier.train(training_set)
accuracy=nltk.classify.util.accuracy(classifier,test_set)

msg1="HI iam giving you 10000000 rs.. don't tell anyone."

words=word_tokenize(msg1)
words=createdec(words)
classifier.classify(words)

	




	