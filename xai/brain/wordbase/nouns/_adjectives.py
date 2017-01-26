

from xai.brain.wordbase.nouns._adjective import _ADJECTIVE

#calss header
class _ADJECTIVES(_ADJECTIVE, ):
	def __init__(self,): 
		_ADJECTIVE.__init__(self)
		self.name = "ADJECTIVES"
		self.specie = 'nouns'
		self.basic = "adjective"
		self.jsondata = {}
