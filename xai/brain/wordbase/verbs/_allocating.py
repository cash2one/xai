

from xai.brain.wordbase.verbs._allocate import _ALLOCATE

#calss header
class _ALLOCATING(_ALLOCATE, ):
	def __init__(self,): 
		_ALLOCATE.__init__(self)
		self.name = "ALLOCATING"
		self.specie = 'verbs'
		self.basic = "allocate"
		self.jsondata = {}
