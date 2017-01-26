

from xai.brain.wordbase.verbs._stiffen import _STIFFEN

#calss header
class _STIFFENED(_STIFFEN, ):
	def __init__(self,): 
		_STIFFEN.__init__(self)
		self.name = "STIFFENED"
		self.specie = 'verbs'
		self.basic = "stiffen"
		self.jsondata = {}
