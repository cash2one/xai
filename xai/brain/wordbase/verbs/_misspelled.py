

from xai.brain.wordbase.verbs._misspell import _MISSPELL

#calss header
class _MISSPELLED(_MISSPELL, ):
	def __init__(self,): 
		_MISSPELL.__init__(self)
		self.name = "MISSPELLED"
		self.specie = 'verbs'
		self.basic = "misspell"
		self.jsondata = {}
