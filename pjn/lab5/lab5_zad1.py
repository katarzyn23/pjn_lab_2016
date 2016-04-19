#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

def markow_from_file(file_name, ngrams_lvl):
	with open(file_name, 'r') as ngrams_file:
		markow_dict = {}
		text=ngrams_file.read().replace('\n', '')
		if ngrams_lvl == 1:
			ngram_list = text.split()
		else:
			ngram_list = prepare_ngrams(text, ngrams_lvl)
		markow_dict = markow_dict_from_list(ngram_list)
		print markow_dict
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
	
def markow_dict_from_list(ngrams_list):
	tmplist = []
	markow_dict = {}
	for ng in ngrams_list:
		for i,j in enumerate(ngrams_list):
			if j==ng:
				if i+1<len(ngrams_list):
					tmplist.append(ngrams_list[i+1])
		markow_dict[ng] = tmplist
		tmplist = []
	return markow_dict
	

lvl = int(sys.argv[2])
ngrams_markow = markow_from_file(sys.argv[1], lvl)