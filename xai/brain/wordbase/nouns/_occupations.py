

from xai.brain.wordbase.nouns._occupation import _OCCUPATION

#calss header
class _OCCUPATIONS(_OCCUPATION, ):
	def __init__(self,): 
		_OCCUPATION.__init__(self)
		self.name = "OCCUPATIONS"
		self.specie = 'nouns'
		self.basic = "occupation"
		self.jsondata = {}
