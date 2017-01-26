

from xai.brain.wordbase.nouns._corpus import _CORPUS

#calss header
class _CORPORA(_CORPUS, ):
	def __init__(self,): 
		_CORPUS.__init__(self)
		self.name = "CORPORA"
		self.specie = 'nouns'
		self.basic = "corpus"
		self.jsondata = {}
