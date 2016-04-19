#!/usr/bin/env python
# -*- coding: utf-8 -*-

import codecs
import random
import sys
from random import randint
import time

def markow_from_pap(file_name, ngrams_lvl):
	markow_dict = {}
	simple_article = ''
	with codecs.open(file_name, 'r', 'utf-8') as pap_file:
		for line in pap_file:
			if line[0] != '#':
				simple_article = simple_article + line	
			else:
				tmp_dict = markow_from_string(simple_article, ngrams_lvl)
				markow_dict = dict(tmp_dict.items() + markow_dict.items())
				simple_article = ''
	return markow_dict
	
def markow_from_string(string_name, ngrams_lvl):
	markow_dict = {}
	ngrams_list = []
	if ngrams_lvl == 1:
		ngrams_list = string_name.split()
	else:
		ngrams_list = prepare_ngrams(string_name, ngrams_lvl)
	tmplist = []
	for ng in ngrams_list:
		for i,j in enumerate(ngrams_list):
			if j==ng:
				if i+1<len(ngrams_list):
					tmplist.append(ngrams_list[i+1])
		markow_dict[ng] = tmplist
		tmplist = []
	return markow_dict
	
def prepare_ngrams(text, ngrams_lvl):
	tmplist = text.split()
	ngram_list = []
	merge_object=''
	counter = 0
	for single_word in tmplist:
		merge_object += single_word + ' '
		counter += 1
		if counter == ngrams_lvl:
			ngram_list.append(merge_object)
			merge_object = ''
			counter = 0
	return ngram_list

def generate_article(first_word, markow_dict):
	article = first_word
	runner = get_one_for_article(markow_dict[first_word])
	for j in range(50):
		article = article + ' ' + runner
		if len(markow_dict[runner]) != 0:
			runner = get_one_for_article(markow_dict[runner])
		else:
			runner = get_one_for_article(markow_dict[random.choice(markow_dict.keys())])
	article += '.'
	return article
	
def get_one_for_article(list):
	if len(list) != 0:
		rand = randint(0,len(list)-1)
		out_list = list[rand]
		return out_list
	else:
		rand = 'w'

start = time.time()
lvl = int(sys.argv[2])
dict = markow_from_pap(sys.argv[1], lvl)
print dict['Stronnictwa']
print generate_article('Stronnictwa', dict)
end = time.time()
print(end - start)
