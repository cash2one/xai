

from xai.brain.wordbase.nouns._disregard import _DISREGARD

#calss header
class _DISREGARDED(_DISREGARD, ):
	def __init__(self,): 
		_DISREGARD.__init__(self)
		self.name = "DISREGARDED"
		self.specie = 'nouns'
		self.basic = "disregard"
		self.jsondata = {}
