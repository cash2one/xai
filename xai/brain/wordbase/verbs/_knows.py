

from xai.brain.wordbase.verbs._know import _KNOW

#calss header
class _KNOWS(_KNOW, ):
	def __init__(self,): 
		_KNOW.__init__(self)
		self.name = "KNOWS"
		self.specie = 'verbs'
		self.basic = "know"
		self.jsondata = {}
