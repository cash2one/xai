

from xai.brain.wordbase.nouns._prefix import _PREFIX

#calss header
class _PREFIXES(_PREFIX, ):
	def __init__(self,): 
		_PREFIX.__init__(self)
		self.name = "PREFIXES"
		self.specie = 'nouns'
		self.basic = "prefix"
		self.jsondata = {}
