

from xai.brain.wordbase.verbs._malfunction import _MALFUNCTION

#calss header
class _MALFUNCTIONED(_MALFUNCTION, ):
	def __init__(self,): 
		_MALFUNCTION.__init__(self)
		self.name = "MALFUNCTIONED"
		self.specie = 'verbs'
		self.basic = "malfunction"
		self.jsondata = {}
