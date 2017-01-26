

from xai.brain.wordbase.nouns._erratum import _ERRATUM

#calss header
class _ERRATA(_ERRATUM, ):
	def __init__(self,): 
		_ERRATUM.__init__(self)
		self.name = "ERRATA"
		self.specie = 'nouns'
		self.basic = "erratum"
		self.jsondata = {}
