

from xai.brain.wordbase.adverbs._piggyback import _PIGGYBACK

#calss header
class _PIGGYBACKED(_PIGGYBACK, ):
	def __init__(self,): 
		_PIGGYBACK.__init__(self)
		self.name = "PIGGYBACKED"
		self.specie = 'adverbs'
		self.basic = "piggyback"
		self.jsondata = {}
