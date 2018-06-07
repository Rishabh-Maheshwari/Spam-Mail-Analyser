import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

with open("email_body.txt","r") as f:
	data=f.read()
	
words=word_tokenize(data)
useful_words=[word for word in words if word not in stopwords.words("English")]

frequency=nltk.FreqDist(useful_words)
print(frequency.most_common(10))