

from xai.brain.wordbase.nouns._catalogue import _CATALOGUE

#calss header
class _CATALOGUES(_CATALOGUE, ):
	def __init__(self,): 
		_CATALOGUE.__init__(self)
		self.name = "CATALOGUES"
		self.specie = 'nouns'
		self.basic = "catalogue"
		self.jsondata = {}
