

from xai.brain.wordbase.nouns._legislator import _LEGISLATOR

#calss header
class _LEGISLATORS(_LEGISLATOR, ):
	def __init__(self,): 
		_LEGISLATOR.__init__(self)
		self.name = "LEGISLATORS"
		self.specie = 'nouns'
		self.basic = "legislator"
		self.jsondata = {}
