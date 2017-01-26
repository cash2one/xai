

from xai.brain.wordbase.verbs._trash import _TRASH

#calss header
class _TRASHED(_TRASH, ):
	def __init__(self,): 
		_TRASH.__init__(self)
		self.name = "TRASHED"
		self.specie = 'verbs'
		self.basic = "trash"
		self.jsondata = {}
