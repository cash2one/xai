

from xai.brain.wordbase.verbs._misspell import _MISSPELL

#calss header
class _MISSPELT(_MISSPELL, ):
	def __init__(self,): 
		_MISSPELL.__init__(self)
		self.name = "MISSPELT"
		self.specie = 'verbs'
		self.basic = "misspell"
		self.jsondata = {}
