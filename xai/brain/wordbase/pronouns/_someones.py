

from xai.brain.wordbase.pronouns._someone import _SOMEONE

#calss header
class _SOMEONES(_SOMEONE, ):
	def __init__(self,): 
		_SOMEONE.__init__(self)
		self.name = "SOMEONES"
		self.specie = 'pronouns'
		self.basic = "someone"
		self.jsondata = {}
