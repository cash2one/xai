

from xai.brain.wordbase.nouns._vocabulary import _VOCABULARY

#calss header
class _VOCABULARIES(_VOCABULARY, ):
	def __init__(self,): 
		_VOCABULARY.__init__(self)
		self.name = "VOCABULARIES"
		self.specie = 'nouns'
		self.basic = "vocabulary"
		self.jsondata = {}
