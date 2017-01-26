

from xai.brain.wordbase.verbs._staff import _STAFF

#calss header
class _STAFFED(_STAFF, ):
	def __init__(self,): 
		_STAFF.__init__(self)
		self.name = "STAFFED"
		self.specie = 'verbs'
		self.basic = "staff"
		self.jsondata = {}
