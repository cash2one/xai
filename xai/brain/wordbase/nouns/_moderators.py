

from xai.brain.wordbase.nouns._moderator import _MODERATOR

#calss header
class _MODERATORS(_MODERATOR, ):
	def __init__(self,): 
		_MODERATOR.__init__(self)
		self.name = "MODERATORS"
		self.specie = 'nouns'
		self.basic = "moderator"
		self.jsondata = {}
