

from xai.brain.wordbase.nouns._people import _PEOPLE

#calss header
class _PEOPLES(_PEOPLE, ):
	def __init__(self,): 
		_PEOPLE.__init__(self)
		self.name = "PEOPLES"
		self.specie = 'nouns'
		self.basic = "people"
		self.jsondata = {}
