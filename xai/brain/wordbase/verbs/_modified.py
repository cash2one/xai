

from xai.brain.wordbase.verbs._modify import _MODIFY

#calss header
class _MODIFIED(_MODIFY, ):
	def __init__(self,): 
		_MODIFY.__init__(self)
		self.name = "MODIFIED"
		self.specie = 'verbs'
		self.basic = "modify"
		self.jsondata = {}
