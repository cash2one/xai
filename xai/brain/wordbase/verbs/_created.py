

from xai.brain.wordbase.verbs._create import _CREATE

#calss header
class _CREATED(_CREATE, ):
	def __init__(self,): 
		_CREATE.__init__(self)
		self.name = "CREATED"
		self.specie = 'verbs'
		self.basic = "create"
		self.jsondata = {}
