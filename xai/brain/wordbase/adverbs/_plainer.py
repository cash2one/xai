

from xai.brain.wordbase.adverbs._plain import _PLAIN

#calss header
class _PLAINER(_PLAIN, ):
	def __init__(self,): 
		_PLAIN.__init__(self)
		self.name = "PLAINER"
		self.specie = 'adverbs'
		self.basic = "plain"
		self.jsondata = {}
