

from xai.brain.wordbase.adverbs._daily import _DAILY

#calss header
class _DAILIES(_DAILY, ):
	def __init__(self,): 
		_DAILY.__init__(self)
		self.name = "DAILIES"
		self.specie = 'adverbs'
		self.basic = "daily"
		self.jsondata = {}
