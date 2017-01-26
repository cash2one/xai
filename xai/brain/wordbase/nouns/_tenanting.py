

from xai.brain.wordbase.nouns._tenant import _TENANT

#calss header
class _TENANTING(_TENANT, ):
	def __init__(self,): 
		_TENANT.__init__(self)
		self.name = "TENANTING"
		self.specie = 'nouns'
		self.basic = "tenant"
		self.jsondata = {}
