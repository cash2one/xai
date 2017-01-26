

from xai.brain.wordbase.verbs._catalogue import _CATALOGUE

#calss header
class _CATALOGUED(_CATALOGUE, ):
	def __init__(self,): 
		_CATALOGUE.__init__(self)
		self.name = "CATALOGUED"
		self.specie = 'verbs'
		self.basic = "catalogue"
		self.jsondata = {}
