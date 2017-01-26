

from xai.brain.wordbase.nouns._daily import _DAILY

#calss header
class _DAILIES(_DAILY, ):
	def __init__(self,): 
		_DAILY.__init__(self)
		self.name = "DAILIES"
		self.specie = 'nouns'
		self.basic = "daily"
		self.jsondata = {}
