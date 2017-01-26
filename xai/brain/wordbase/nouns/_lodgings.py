

from xai.brain.wordbase.nouns._lodging import _LODGING

#calss header
class _LODGINGS(_LODGING, ):
	def __init__(self,): 
		_LODGING.__init__(self)
		self.name = "LODGINGS"
		self.specie = 'nouns'
		self.basic = "lodging"
		self.jsondata = {}
