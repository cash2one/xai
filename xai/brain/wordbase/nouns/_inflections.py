

from xai.brain.wordbase.nouns._inflection import _INFLECTION

#calss header
class _INFLECTIONS(_INFLECTION, ):
	def __init__(self,): 
		_INFLECTION.__init__(self)
		self.name = "INFLECTIONS"
		self.specie = 'nouns'
		self.basic = "inflection"
		self.jsondata = {}
