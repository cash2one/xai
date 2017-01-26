

from xai.brain.wordbase.verbs._declassify import _DECLASSIFY

#calss header
class _DECLASSIFIED(_DECLASSIFY, ):
	def __init__(self,): 
		_DECLASSIFY.__init__(self)
		self.name = "DECLASSIFIED"
		self.specie = 'verbs'
		self.basic = "declassify"
		self.jsondata = {}
