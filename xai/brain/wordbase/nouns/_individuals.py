

from xai.brain.wordbase.nouns._individual import _INDIVIDUAL

#calss header
class _INDIVIDUALS(_INDIVIDUAL, ):
	def __init__(self,): 
		_INDIVIDUAL.__init__(self)
		self.name = "INDIVIDUALS"
		self.specie = 'nouns'
		self.basic = "individual"
		self.jsondata = {}
