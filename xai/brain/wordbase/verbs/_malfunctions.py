

from xai.brain.wordbase.verbs._malfunction import _MALFUNCTION

#calss header
class _MALFUNCTIONS(_MALFUNCTION, ):
	def __init__(self,): 
		_MALFUNCTION.__init__(self)
		self.name = "MALFUNCTIONS"
		self.specie = 'verbs'
		self.basic = "malfunction"
		self.jsondata = {}
