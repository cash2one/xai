

from xai.brain.wordbase.nouns._professional import _PROFESSIONAL

#calss header
class _PROFESSIONALS(_PROFESSIONAL, ):
	def __init__(self,): 
		_PROFESSIONAL.__init__(self)
		self.name = "PROFESSIONALS"
		self.specie = 'nouns'
		self.basic = "professional"
		self.jsondata = {}
