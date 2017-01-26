

from xai.brain.wordbase.verbs._browse import _BROWSE

#calss header
class _BROWSED(_BROWSE, ):
	def __init__(self,): 
		_BROWSE.__init__(self)
		self.name = "BROWSED"
		self.specie = 'verbs'
		self.basic = "browse"
		self.jsondata = {}
