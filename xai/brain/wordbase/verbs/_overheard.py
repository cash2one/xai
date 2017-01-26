

from xai.brain.wordbase.verbs._overhear import _OVERHEAR

#calss header
class _OVERHEARD(_OVERHEAR, ):
	def __init__(self,): 
		_OVERHEAR.__init__(self)
		self.name = "OVERHEARD"
		self.specie = 'verbs'
		self.basic = "overhear"
		self.jsondata = {}
