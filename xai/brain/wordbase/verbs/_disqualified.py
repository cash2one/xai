

from xai.brain.wordbase.verbs._disqualify import _DISQUALIFY

#calss header
class _DISQUALIFIED(_DISQUALIFY, ):
	def __init__(self,): 
		_DISQUALIFY.__init__(self)
		self.name = "DISQUALIFIED"
		self.specie = 'verbs'
		self.basic = "disqualify"
		self.jsondata = {}
