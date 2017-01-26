

from xai.brain.wordbase.nouns._alumnus import _ALUMNUS

#calss header
class _ALUMNI(_ALUMNUS, ):
	def __init__(self,): 
		_ALUMNUS.__init__(self)
		self.name = "ALUMNI"
		self.specie = 'nouns'
		self.basic = "alumnus"
		self.jsondata = {}
