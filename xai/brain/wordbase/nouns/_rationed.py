

from xai.brain.wordbase.nouns._ration import _RATION

#calss header
class _RATIONED(_RATION, ):
	def __init__(self,): 
		_RATION.__init__(self)
		self.name = "RATIONED"
		self.specie = 'nouns'
		self.basic = "ration"
		self.jsondata = {}
