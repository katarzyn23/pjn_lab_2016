#!/usr/bin/env python

import codecs
from collections import Counter
from random import randint

def markow_from_file(fileName):
	with open(fileName, 'r') as ngramsFile:
		ngrams=ngramsFile.read().replace('\n', '')
		ngramsList = ngrams.split()
		tmplist = []
		for ng in ngramsList:
			for i,j in enumerate(ngramsList):
				if j==ng:
					if i+1<len(ngramsList):
						tmplist.append(ngramsList[i+1])
			markowDict[ng] = tmplist
			tmplist = []
		print markowDict
	return markowDict
	
	
def markow_from_string(stringName):
	markowDict = {}
	ngramsList = stringName.split()
	tmplist = []
	for ng in ngramsList:
		for i,j in enumerate(ngramsList):
			if j==ng:
				if i+1<len(ngramsList):
					tmplist.append(ngramsList[i+1])
		markowDict[ng] = tmplist
		tmplist = []
	return markowDict
	
	
with open('pap_small.txt', 'r') as ngramsFile:
	ngrams=ngramsFile.read().replace('\n', '')
	ngramsList = ngrams.split()
		
		
def get_one_of(list):
	if len(list) != 0:
		rand = randint(0,len(list)-1)
		return list.pop(rand)
	else:
		rand = 'w'
		
def generate_article(first_word, markowDict):
	article = first_word
	runner = get_one_of(markowDict[first_word])
	for j in range(50):
		article = article + ' ' + runner
		runner = get_one_of(markowDict[runner])
	return article
	
def markow_from_pap():
	markowDict = {}
	simpleArticle = ""
	i = 1
	with codecs.open('pap_small.txt', 'r', 'utf-8') as papFile:
		for line in papFile:
			if line[0] != '#':
				simpleArticle = simpleArticle + line	
			else:
				tmpDict = markow_from_string(simpleArticle)
				markowDict = dict(tmpDict.items() + markowDict.items())
				simpleArticle = ''
	return markowDict

#cw1 - markow chain from ngrams
ngrams_markow = markow_from_file

#cw2 - generated article from pap
dict = markow_from_pap()
print generate_article('Madeleine', dict)

#cw3 - generated polish word


			
		
		
		
		