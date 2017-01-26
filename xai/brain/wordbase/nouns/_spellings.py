

from xai.brain.wordbase.nouns._spelling import _SPELLING

#calss header
class _SPELLINGS(_SPELLING, ):
	def __init__(self,): 
		_SPELLING.__init__(self)
		self.name = "SPELLINGS"
		self.specie = 'nouns'
		self.basic = "spelling"
		self.jsondata = {}
