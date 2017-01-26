

from xai.brain.wordbase.nouns._vote import _VOTE

#calss header
class _VOTED(_VOTE, ):
	def __init__(self,): 
		_VOTE.__init__(self)
		self.name = "VOTED"
		self.specie = 'nouns'
		self.basic = "vote"
		self.jsondata = {}
