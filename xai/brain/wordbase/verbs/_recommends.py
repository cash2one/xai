

from xai.brain.wordbase.verbs._recommend import _RECOMMEND

#calss header
class _RECOMMENDS(_RECOMMEND, ):
	def __init__(self,): 
		_RECOMMEND.__init__(self)
		self.name = "RECOMMENDS"
		self.specie = 'verbs'
		self.basic = "recommend"
		self.jsondata = {}
