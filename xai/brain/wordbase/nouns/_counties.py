

from xai.brain.wordbase.nouns._county import _COUNTY

#calss header
class _COUNTIES(_COUNTY, ):
	def __init__(self,): 
		_COUNTY.__init__(self)
		self.name = "COUNTIES"
		self.specie = 'nouns'
		self.basic = "county"
		self.jsondata = {}
