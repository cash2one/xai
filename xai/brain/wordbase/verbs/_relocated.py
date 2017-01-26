

from xai.brain.wordbase.verbs._relocate import _RELOCATE

#calss header
class _RELOCATED(_RELOCATE, ):
	def __init__(self,): 
		_RELOCATE.__init__(self)
		self.name = "RELOCATED"
		self.specie = 'verbs'
		self.basic = "relocate"
		self.jsondata = {}
