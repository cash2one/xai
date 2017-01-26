

from xai.brain.wordbase.verbs._embolden import _EMBOLDEN

#calss header
class _EMBOLDENED(_EMBOLDEN, ):
	def __init__(self,): 
		_EMBOLDEN.__init__(self)
		self.name = "EMBOLDENED"
		self.specie = 'verbs'
		self.basic = "embolden"
		self.jsondata = {}
