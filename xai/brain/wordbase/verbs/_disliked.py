

from xai.brain.wordbase.verbs._dislike import _DISLIKE

#calss header
class _DISLIKED(_DISLIKE, ):
	def __init__(self,): 
		_DISLIKE.__init__(self)
		self.name = "DISLIKED"
		self.specie = 'verbs'
		self.basic = "dislike"
		self.jsondata = {}
