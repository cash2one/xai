

from xai.brain.wordbase.verbs._castle import _CASTLE

#calss header
class _CASTLING(_CASTLE, ):
	def __init__(self,): 
		_CASTLE.__init__(self)
		self.name = "CASTLING"
		self.specie = 'verbs'
		self.basic = "castle"
		self.jsondata = {}
