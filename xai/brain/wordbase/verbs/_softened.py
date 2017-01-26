

from xai.brain.wordbase.verbs._soften import _SOFTEN

#calss header
class _SOFTENED(_SOFTEN, ):
	def __init__(self,): 
		_SOFTEN.__init__(self)
		self.name = "SOFTENED"
		self.specie = 'verbs'
		self.basic = "soften"
		self.jsondata = {}
