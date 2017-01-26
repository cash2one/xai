

from xai.brain.wordbase.verbs._downgrade import _DOWNGRADE

#calss header
class _DOWNGRADED(_DOWNGRADE, ):
	def __init__(self,): 
		_DOWNGRADE.__init__(self)
		self.name = "DOWNGRADED"
		self.specie = 'verbs'
		self.basic = "downgrade"
		self.jsondata = {}
