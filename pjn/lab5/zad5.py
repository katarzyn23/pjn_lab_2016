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
	
	
def get_one_of(list):
	if len(list) != 0:
		rand = randint(0,len(list)-1)
		return list.pop(rand)
	else:
		return 'w'

markowDict = {}
simpleArticle = ""
i = 1
with codecs.open('pap.txt', 'r', 'utf-8') as papFile:
	for line in papFile:
		if line[0] != '#':
			simpleArticle = simpleArticle + line	
		else:
			tmpDict = markow_from_string(simpleArticle)
			markowDict = dict(tmpDict.items() + markowDict.items())
			simpleArticle = ''

			
out = 'Rewanzowy'
runner = get_one_of(markowDict[out])
out = out + ' ' + runner
for j in range(50):
	runner = get_one_of(markowDict[runner])
	out = out + ' ' + runner
print out
			
		
		
		
		