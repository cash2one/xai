

from xai.brain.wordbase.nouns._browse import _BROWSE

#calss header
class _BROWSED(_BROWSE, ):
	def __init__(self,): 
		_BROWSE.__init__(self)
		self.name = "BROWSED"
		self.specie = 'nouns'
		self.basic = "browse"
		self.jsondata = {}
