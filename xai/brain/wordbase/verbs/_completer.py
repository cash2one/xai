

from xai.brain.wordbase.verbs._complete import _COMPLETE

#calss header
class _COMPLETER(_COMPLETE, ):
	def __init__(self,): 
		_COMPLETE.__init__(self)
		self.name = "COMPLETER"
		self.specie = 'verbs'
		self.basic = "complete"
		self.jsondata = {}
