

from xai.brain.wordbase.verbs._entail import _ENTAIL

#calss header
class _ENTAILS(_ENTAIL, ):
	def __init__(self,): 
		_ENTAIL.__init__(self)
		self.name = "ENTAILS"
		self.specie = 'verbs'
		self.basic = "entail"
		self.jsondata = {}
