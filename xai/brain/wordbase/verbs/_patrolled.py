

from xai.brain.wordbase.verbs._patrol import _PATROL

#calss header
class _PATROLLED(_PATROL, ):
	def __init__(self,): 
		_PATROL.__init__(self)
		self.name = "PATROLLED"
		self.specie = 'verbs'
		self.basic = "patrol"
		self.jsondata = {}
