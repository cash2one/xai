

from xai.brain.wordbase.verbs._punctuate import _PUNCTUATE

#calss header
class _PUNCTUATED(_PUNCTUATE, ):
	def __init__(self,): 
		_PUNCTUATE.__init__(self)
		self.name = "PUNCTUATED"
		self.specie = 'verbs'
		self.basic = "punctuate"
		self.jsondata = {}
