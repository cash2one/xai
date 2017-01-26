

from xai.brain.wordbase.nouns._plain import _PLAIN

#calss header
class _PLAINER(_PLAIN, ):
	def __init__(self,): 
		_PLAIN.__init__(self)
		self.name = "PLAINER"
		self.specie = 'nouns'
		self.basic = "plain"
		self.jsondata = {}
