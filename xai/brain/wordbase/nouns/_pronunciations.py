

from xai.brain.wordbase.nouns._pronunciation import _PRONUNCIATION

#calss header
class _PRONUNCIATIONS(_PRONUNCIATION, ):
	def __init__(self,): 
		_PRONUNCIATION.__init__(self)
		self.name = "PRONUNCIATIONS"
		self.specie = 'nouns'
		self.basic = "pronunciation"
		self.jsondata = {}
