

from xai.brain.wordbase.nouns._charity import _CHARITY

#calss header
class _CHARITIES(_CHARITY, ):
	def __init__(self,): 
		_CHARITY.__init__(self)
		self.name = "CHARITIES"
		self.specie = 'nouns'
		self.basic = "charity"
		self.jsondata = {}
