

from xai.brain.wordbase.nouns._tenant import _TENANT

#calss header
class _TENANTED(_TENANT, ):
	def __init__(self,): 
		_TENANT.__init__(self)
		self.name = "TENANTED"
		self.specie = 'nouns'
		self.basic = "tenant"
		self.jsondata = {}
