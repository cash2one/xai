

from xai.brain.wordbase.verbs._entail import _ENTAIL

#calss header
class _ENTAILING(_ENTAIL, ):
	def __init__(self,): 
		_ENTAIL.__init__(self)
		self.name = "ENTAILING"
		self.specie = 'verbs'
		self.basic = "entail"
		self.jsondata = {}
