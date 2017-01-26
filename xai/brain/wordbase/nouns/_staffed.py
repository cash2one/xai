

from xai.brain.wordbase.nouns._staff import _STAFF

#calss header
class _STAFFED(_STAFF, ):
	def __init__(self,): 
		_STAFF.__init__(self)
		self.name = "STAFFED"
		self.specie = 'nouns'
		self.basic = "staff"
		self.jsondata = {}
