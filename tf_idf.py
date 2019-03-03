import os
import math
import collections

lem_docs_path = 'lemmatization/'
index_path = 'index/'

docs_list = os.listdir(lem_docs_path)
docs_all_words = {}
in_dict = {}
tf_idf = {}

for item in docs_list:
    with open(lem_docs_path + item, encoding='utf-8') as file:
        doc_num = int(item.split('.')[0])
        words = file.readline().split('\t')
        docs_all_words[doc_num - 1] = len(words)
    for word in words:
    	if word == '':
            continue
    	if word not in in_dict:
    		in_dict[word] = [0] * len(docs_list)
    	in_dict[word][doc_num - 1] = 1

for word in in_dict.keys():
    for doc_index in range(len(docs_list)):
        tf = in_dict[word][doc_index] / docs_all_words[doc_index]
        idf = math.log10(len(docs_list) / collections.Counter(in_dict[word])[1])
        if word not in tf_idf:
        	tf_idf[word] = [0] * len(docs_list)
        tf_idf[word][doc_index] = tf * idf

for word, values in tf_idf.items():
	with open(index_path + word + '.txt', "w") as file:
		for value in values:
			file.write(str(value) + '\n')