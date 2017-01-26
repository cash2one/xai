

from xai.brain.wordbase.verbs._ration import _RATION

#calss header
class _RATIONED(_RATION, ):
	def __init__(self,): 
		_RATION.__init__(self)
		self.name = "RATIONED"
		self.specie = 'verbs'
		self.basic = "ration"
		self.jsondata = {}
