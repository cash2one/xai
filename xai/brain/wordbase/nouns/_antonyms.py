

from xai.brain.wordbase.nouns._antonym import _ANTONYM

#calss header
class _ANTONYMS(_ANTONYM, ):
	def __init__(self,): 
		_ANTONYM.__init__(self)
		self.name = "ANTONYMS"
		self.specie = 'nouns'
		self.basic = "antonym"
		self.jsondata = {}
