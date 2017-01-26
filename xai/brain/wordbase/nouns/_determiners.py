

from xai.brain.wordbase.nouns._determiner import _DETERMINER

#calss header
class _DETERMINERS(_DETERMINER, ):
	def __init__(self,): 
		_DETERMINER.__init__(self)
		self.name = "DETERMINERS"
		self.specie = 'nouns'
		self.basic = "determiner"
		self.jsondata = {}
