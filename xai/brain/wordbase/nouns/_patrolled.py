

from xai.brain.wordbase.nouns._patrol import _PATROL

#calss header
class _PATROLLED(_PATROL, ):
	def __init__(self,): 
		_PATROL.__init__(self)
		self.name = "PATROLLED"
		self.specie = 'nouns'
		self.basic = "patrol"
		self.jsondata = {}
