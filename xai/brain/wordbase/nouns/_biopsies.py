

from xai.brain.wordbase.nouns._biopsy import _BIOPSY

#calss header
class _BIOPSIES(_BIOPSY, ):
	def __init__(self,): 
		_BIOPSY.__init__(self)
		self.name = "BIOPSIES"
		self.specie = 'nouns'
		self.basic = "biopsy"
		self.jsondata = {}
