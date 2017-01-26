

from xai.brain.wordbase.verbs._intensify import _INTENSIFY

#calss header
class _INTENSIFIED(_INTENSIFY, ):
	def __init__(self,): 
		_INTENSIFY.__init__(self)
		self.name = "INTENSIFIED"
		self.specie = 'verbs'
		self.basic = "intensify"
		self.jsondata = {}
