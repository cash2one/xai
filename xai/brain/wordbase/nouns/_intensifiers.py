

from xai.brain.wordbase.nouns._intensifier import _INTENSIFIER

#calss header
class _INTENSIFIERS(_INTENSIFIER, ):
	def __init__(self,): 
		_INTENSIFIER.__init__(self)
		self.name = "INTENSIFIERS"
		self.specie = 'nouns'
		self.basic = "intensifier"
		self.jsondata = {}
