

from xai.brain.wordbase.verbs._collocate import _COLLOCATE

#calss header
class _COLLOCATES(_COLLOCATE, ):
	def __init__(self,): 
		_COLLOCATE.__init__(self)
		self.name = "COLLOCATES"
		self.specie = 'verbs'
		self.basic = "collocate"
		self.jsondata = {}
