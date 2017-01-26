

from xai.brain.wordbase.nouns._allergy import _ALLERGY

#calss header
class _ALLERGIES(_ALLERGY, ):
	def __init__(self,): 
		_ALLERGY.__init__(self)
		self.name = "ALLERGIES"
		self.specie = 'nouns'
		self.basic = "allergy"
		self.jsondata = {}
