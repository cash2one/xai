

from xai.brain.wordbase.nouns._psychotherapist import _PSYCHOTHERAPIST

#calss header
class _PSYCHOTHERAPISTS(_PSYCHOTHERAPIST, ):
	def __init__(self,): 
		_PSYCHOTHERAPIST.__init__(self)
		self.name = "PSYCHOTHERAPISTS"
		self.specie = 'nouns'
		self.basic = "psychotherapist"
		self.jsondata = {}
