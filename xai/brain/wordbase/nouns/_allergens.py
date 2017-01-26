

from xai.brain.wordbase.nouns._allergen import _ALLERGEN

#calss header
class _ALLERGENS(_ALLERGEN, ):
	def __init__(self,): 
		_ALLERGEN.__init__(self)
		self.name = "ALLERGENS"
		self.specie = 'nouns'
		self.basic = "allergen"
		self.jsondata = {}
