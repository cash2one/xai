

from xai.brain.wordbase.verbs._rebuff import _REBUFF

#calss header
class _REBUFFED(_REBUFF, ):
	def __init__(self,): 
		_REBUFF.__init__(self)
		self.name = "REBUFFED"
		self.specie = 'verbs'
		self.basic = "rebuff"
		self.jsondata = {}
