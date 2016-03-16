# -*- coding: utf-8 -*-
from sets import Set
import sys

howManyGram = 3
print ("n = ", howManyGram)
sentence = sys.argv[1:2].pop()
sentenceVector = Set([])
splittedSentences = sentence.split(" ")
for sent in splittedSentences:
	n=0
	while (n<len(sent)):
		sentenceVector.add(sent[n:n+howManyGram])
		n=n+1
		pass

print sentenceVector
print len(sentence)
files= ['finnish.txt', 'polski.txt',  'q.txt']
for language in files:
	with open("pjn_lab1/"+language, "r") as inputFile:
		inFileAsString = inputFile.read()
		vector = Set([])
		splittedWords = inFileAsString.split(" ")
		for word in splittedWords:
			n=0
			while (n < len(word)):
				vector.add(word[n:n+howManyGram])
				n=n+1
				pass
		print (language, " ", len(vector))
		counter=0
		for ngram in sentenceVector:
			if(ngram in vector):
				counter=counter+1
			pass
		print (counter, " / ", len(sentence))
