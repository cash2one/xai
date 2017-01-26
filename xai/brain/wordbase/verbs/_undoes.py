

from xai.brain.wordbase.verbs._undo import _UNDO

#calss header
class _UNDOES(_UNDO, ):
	def __init__(self,): 
		_UNDO.__init__(self)
		self.name = "UNDOES"
		self.specie = 'verbs'
		self.basic = "undo"
		self.jsondata = {}
