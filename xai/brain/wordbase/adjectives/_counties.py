

from xai.brain.wordbase.adjectives._county import _COUNTY

#calss header
class _COUNTIES(_COUNTY, ):
	def __init__(self,): 
		_COUNTY.__init__(self)
		self.name = "COUNTIES"
		self.specie = 'adjectives'
		self.basic = "county"
		self.jsondata = {}
