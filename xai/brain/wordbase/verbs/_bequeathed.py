

from xai.brain.wordbase.verbs._bequeath import _BEQUEATH

#calss header
class _BEQUEATHED(_BEQUEATH, ):
	def __init__(self,): 
		_BEQUEATH.__init__(self)
		self.name = "BEQUEATHED"
		self.specie = 'verbs'
		self.basic = "bequeath"
		self.jsondata = {}
