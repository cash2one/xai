

from xai.brain.wordbase.verbs._prohibit import _PROHIBIT

#calss header
class _PROHIBITED(_PROHIBIT, ):
	def __init__(self,): 
		_PROHIBIT.__init__(self)
		self.name = "PROHIBITED"
		self.specie = 'verbs'
		self.basic = "prohibit"
		self.jsondata = {}
