

from xai.brain.wordbase.verbs._blacken import _BLACKEN

#calss header
class _BLACKENED(_BLACKEN, ):
	def __init__(self,): 
		_BLACKEN.__init__(self)
		self.name = "BLACKENED"
		self.specie = 'verbs'
		self.basic = "blacken"
		self.jsondata = {}
