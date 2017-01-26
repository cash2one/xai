

from xai.brain.wordbase.verbs._migrate import _MIGRATE

#calss header
class _MIGRATING(_MIGRATE, ):
	def __init__(self,): 
		_MIGRATE.__init__(self)
		self.name = "MIGRATING"
		self.specie = 'verbs'
		self.basic = "migrate"
		self.jsondata = {}
