

from xai.brain.wordbase.verbs._misspelling import _MISSPELLING

#calss header
class _MISSPELLINGS(_MISSPELLING, ):
	def __init__(self,): 
		_MISSPELLING.__init__(self)
		self.name = "MISSPELLINGS"
		self.specie = 'verbs'
		self.basic = "misspelling"
		self.jsondata = {}
