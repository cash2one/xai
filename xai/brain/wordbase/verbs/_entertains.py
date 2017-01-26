

from xai.brain.wordbase.verbs._entertain import _ENTERTAIN

#calss header
class _ENTERTAINS(_ENTERTAIN, ):
	def __init__(self,): 
		_ENTERTAIN.__init__(self)
		self.name = "ENTERTAINS"
		self.specie = 'verbs'
		self.basic = "entertain"
		self.jsondata = {}
