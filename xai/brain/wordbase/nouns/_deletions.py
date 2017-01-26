

from xai.brain.wordbase.nouns._deletion import _DELETION

#calss header
class _DELETIONS(_DELETION, ):
	def __init__(self,): 
		_DELETION.__init__(self)
		self.name = "DELETIONS"
		self.specie = 'nouns'
		self.basic = "deletion"
		self.jsondata = {}
