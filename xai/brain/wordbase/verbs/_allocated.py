

from xai.brain.wordbase.verbs._allocate import _ALLOCATE

#calss header
class _ALLOCATED(_ALLOCATE, ):
	def __init__(self,): 
		_ALLOCATE.__init__(self)
		self.name = "ALLOCATED"
		self.specie = 'verbs'
		self.basic = "allocate"
		self.jsondata = {}
