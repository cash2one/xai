

from xai.brain.wordbase.verbs._entail import _ENTAIL

#calss header
class _ENTAILED(_ENTAIL, ):
	def __init__(self,): 
		_ENTAIL.__init__(self)
		self.name = "ENTAILED"
		self.specie = 'verbs'
		self.basic = "entail"
		self.jsondata = {}
