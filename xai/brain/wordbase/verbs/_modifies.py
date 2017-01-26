

from xai.brain.wordbase.verbs._modify import _MODIFY

#calss header
class _MODIFIES(_MODIFY, ):
	def __init__(self,): 
		_MODIFY.__init__(self)
		self.name = "MODIFIES"
		self.specie = 'verbs'
		self.basic = "modify"
		self.jsondata = {}
