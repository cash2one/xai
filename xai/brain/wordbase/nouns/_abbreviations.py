

from xai.brain.wordbase.nouns._abbreviation import _ABBREVIATION

#calss header
class _ABBREVIATIONS(_ABBREVIATION, ):
	def __init__(self,): 
		_ABBREVIATION.__init__(self)
		self.name = "ABBREVIATIONS"
		self.specie = 'nouns'
		self.basic = "abbreviation"
		self.jsondata = {}
