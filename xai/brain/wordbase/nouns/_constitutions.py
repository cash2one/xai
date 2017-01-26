

from xai.brain.wordbase.nouns._constitution import _CONSTITUTION

#calss header
class _CONSTITUTIONS(_CONSTITUTION, ):
	def __init__(self,): 
		_CONSTITUTION.__init__(self)
		self.name = "CONSTITUTIONS"
		self.specie = 'nouns'
		self.basic = "constitution"
		self.jsondata = {}
