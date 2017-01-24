#!/usr/bin/env python
from WikiParse import WiktionaryParser
parser = WiktionaryParser()
word = parser.fetch('apple')
# print(word[0]['definitions'])

for job in word[0]['definitions'][0]:
	print(job)
#
print('\ndefinitions')
print('----------------------------------------------')
print(word[0]['definitions'][0]['text'])


resutl = [(Chunk Paper/NN is/VBZ a/DT thin/JJ material/NN)]
print(resutl)