

from xai.brain.wordbase.verbs._collocate import _COLLOCATE

#calss header
class _COLLOCATED(_COLLOCATE, ):
	def __init__(self,): 
		_COLLOCATE.__init__(self)
		self.name = "COLLOCATED"
		self.specie = 'verbs'
		self.basic = "collocate"
		self.jsondata = {}
