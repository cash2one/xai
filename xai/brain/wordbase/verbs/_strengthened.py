

from xai.brain.wordbase.verbs._strengthen import _STRENGTHEN

#calss header
class _STRENGTHENED(_STRENGTHEN, ):
	def __init__(self,): 
		_STRENGTHEN.__init__(self)
		self.name = "STRENGTHENED"
		self.specie = 'verbs'
		self.basic = "strengthen"
		self.jsondata = {}
