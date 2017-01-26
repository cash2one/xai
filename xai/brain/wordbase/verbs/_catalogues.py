

from xai.brain.wordbase.verbs._catalogue import _CATALOGUE

#calss header
class _CATALOGUES(_CATALOGUE, ):
	def __init__(self,): 
		_CATALOGUE.__init__(self)
		self.name = "CATALOGUES"
		self.specie = 'verbs'
		self.basic = "catalogue"
		self.jsondata = {}
