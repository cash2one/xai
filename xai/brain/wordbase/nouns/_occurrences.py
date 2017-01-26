

from xai.brain.wordbase.nouns._occurrence import _OCCURRENCE

#calss header
class _OCCURRENCES(_OCCURRENCE, ):
	def __init__(self,): 
		_OCCURRENCE.__init__(self)
		self.name = "OCCURRENCES"
		self.specie = 'nouns'
		self.basic = "occurrence"
		self.jsondata = {}
