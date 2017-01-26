

from xai.brain.wordbase.verbs._boycott import _BOYCOTT

#calss header
class _BOYCOTTED(_BOYCOTT, ):
	def __init__(self,): 
		_BOYCOTT.__init__(self)
		self.name = "BOYCOTTED"
		self.specie = 'verbs'
		self.basic = "boycott"
		self.jsondata = {}
