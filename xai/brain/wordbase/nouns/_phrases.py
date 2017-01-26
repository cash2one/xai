

from xai.brain.wordbase.nouns._phrase import _PHRASE

#calss header
class _PHRASES(_PHRASE, ):
	def __init__(self,): 
		_PHRASE.__init__(self)
		self.name = "PHRASES"
		self.specie = 'nouns'
		self.basic = "phrase"
		self.jsondata = {}
