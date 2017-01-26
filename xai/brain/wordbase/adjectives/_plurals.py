

from xai.brain.wordbase.adjectives._plural import _PLURAL

#calss header
class _PLURALS(_PLURAL, ):
	def __init__(self,): 
		_PLURAL.__init__(self)
		self.name = "PLURALS"
		self.specie = 'adjectives'
		self.basic = "plural"
		self.jsondata = {}
