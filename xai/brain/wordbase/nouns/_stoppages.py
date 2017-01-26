

from xai.brain.wordbase.nouns._stoppage import _STOPPAGE

#calss header
class _STOPPAGES(_STOPPAGE, ):
	def __init__(self,): 
		_STOPPAGE.__init__(self)
		self.name = "STOPPAGES"
		self.specie = 'nouns'
		self.basic = "stoppage"
		self.jsondata = {}
