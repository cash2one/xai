

from xai.brain.wordbase.verbs._sanction import _SANCTION

#calss header
class _SANCTIONED(_SANCTION, ):
	def __init__(self,): 
		_SANCTION.__init__(self)
		self.name = "SANCTIONED"
		self.specie = 'verbs'
		self.basic = "sanction"
		self.jsondata = {}
