

from xai.brain.wordbase.nouns._extract import _EXTRACT

#calss header
class _EXTRACTS(_EXTRACT, ):
	def __init__(self,): 
		_EXTRACT.__init__(self)
		self.name = "EXTRACTS"
		self.specie = 'nouns'
		self.basic = "extract"
		self.jsondata = {}
