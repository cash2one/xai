

from xai.brain.wordbase.verbs._cleanse import _CLEANSE

#calss header
class _CLEANSED(_CLEANSE, ):
	def __init__(self,): 
		_CLEANSE.__init__(self)
		self.name = "CLEANSED"
		self.specie = 'verbs'
		self.basic = "cleanse"
		self.jsondata = {}
