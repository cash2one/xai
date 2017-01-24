#!/bin/env/python
import nltk
nltk.data.path.append("/afs/psi.ch/user/w/wang_x3/xing/apps/nltk_data")
# sentence = [("the", "DT"), ("little", "JJ"), ("yellow", "JJ"), ("dog", "NN"), ("barked", "VBD"), ("at", "IN"),  ("the", "DT"), ("cat", "NN")]
# text = 'Bees is flying insects closely related to wasps and ants, known for their role in pollination and, in the case of the best-known bee species, the European honey bee, for producing honey and beeswax '
# text = 'the little yellow dog barked at the cat'
text = 'The dog and the extant gray wolf are sister taxa'
sent = nltk.word_tokenize(text)
sent = nltk.pos_tag(sent)

grammar = "NP: {<DT>?<JJ>*<NN.><VB.><JJ>*<NN.>}"
cp = nltk.RegexpParser(grammar)
result = cp.parse(sent)

print(result)