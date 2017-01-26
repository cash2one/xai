

from xai.brain.wordbase.nouns._decline import _DECLINE

#calss header
class _DECLINING(_DECLINE, ):
	def __init__(self,): 
		_DECLINE.__init__(self)
		self.name = "DECLINING"
		self.specie = 'nouns'
		self.basic = "decline"
		self.jsondata = {}
