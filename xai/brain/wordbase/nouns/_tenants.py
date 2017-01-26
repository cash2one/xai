

from xai.brain.wordbase.nouns._tenant import _TENANT

#calss header
class _TENANTS(_TENANT, ):
	def __init__(self,): 
		_TENANT.__init__(self)
		self.name = "TENANTS"
		self.specie = 'nouns'
		self.basic = "tenant"
		self.jsondata = {}
