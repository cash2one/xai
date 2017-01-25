

from xai.brain.wordbase.nouns._complement import _COMPLEMENT

#calss header
class _COMPLEMENTED(_COMPLEMENT, ):
	def __init__(self,): 
		_COMPLEMENT.__init__(self)
		self.name = "COMPLEMENTED"
		self.specie = 'nouns'
		self.basic = "complement"
		self.jsondata = {}
