

from xai.brain.wordbase.nouns._trash import _TRASH

#calss header
class _TRASHED(_TRASH, ):
	def __init__(self,): 
		_TRASH.__init__(self)
		self.name = "TRASHED"
		self.specie = 'nouns'
		self.basic = "trash"
		self.jsondata = {}
