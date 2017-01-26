

from xai.brain.wordbase.verbs._create import _CREATE

#calss header
class _CREATES(_CREATE, ):
	def __init__(self,): 
		_CREATE.__init__(self)
		self.name = "CREATES"
		self.specie = 'verbs'
		self.basic = "create"
		self.jsondata = {}
