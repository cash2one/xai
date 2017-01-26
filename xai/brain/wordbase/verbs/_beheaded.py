

from xai.brain.wordbase.verbs._behead import _BEHEAD

#calss header
class _BEHEADED(_BEHEAD, ):
	def __init__(self,): 
		_BEHEAD.__init__(self)
		self.name = "BEHEADED"
		self.specie = 'verbs'
		self.basic = "behead"
		self.jsondata = {}
