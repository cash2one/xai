

from xai.brain.wordbase.verbs._overhear import _OVERHEAR

#calss header
class _OVERHEARING(_OVERHEAR, ):
	def __init__(self,): 
		_OVERHEAR.__init__(self)
		self.name = "OVERHEARING"
		self.specie = 'verbs'
		self.basic = "overhear"
		self.jsondata = {}
