

from xai.brain.wordbase.nouns._gender import _GENDER

#calss header
class _GENDERS(_GENDER, ):
	def __init__(self,): 
		_GENDER.__init__(self)
		self.name = "GENDERS"
		self.specie = 'nouns'
		self.basic = "gender"
		self.jsondata = {}
