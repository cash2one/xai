

from xai.brain.wordbase.verbs._migrate import _MIGRATE

#calss header
class _MIGRATED(_MIGRATE, ):
	def __init__(self,): 
		_MIGRATE.__init__(self)
		self.name = "MIGRATED"
		self.specie = 'verbs'
		self.basic = "migrate"
		self.jsondata = {}
