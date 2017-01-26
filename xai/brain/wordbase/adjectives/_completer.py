

from xai.brain.wordbase.adjectives._complete import _COMPLETE

#calss header
class _COMPLETER(_COMPLETE, ):
	def __init__(self,): 
		_COMPLETE.__init__(self)
		self.name = "COMPLETER"
		self.specie = 'adjectives'
		self.basic = "complete"
		self.jsondata = {}
