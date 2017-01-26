

from xai.brain.wordbase.nouns._holding import _HOLDING

#calss header
class _HOLDINGS(_HOLDING, ):
	def __init__(self,): 
		_HOLDING.__init__(self)
		self.name = "HOLDINGS"
		self.specie = 'nouns'
		self.basic = "holding"
		self.jsondata = {}
