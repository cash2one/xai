

from xai.brain.wordbase.verbs._repossess import _REPOSSESS

#calss header
class _REPOSSESSED(_REPOSSESS, ):
	def __init__(self,): 
		_REPOSSESS.__init__(self)
		self.name = "REPOSSESSED"
		self.specie = 'verbs'
		self.basic = "repossess"
		self.jsondata = {}
