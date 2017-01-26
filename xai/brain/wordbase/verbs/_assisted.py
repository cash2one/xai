

from xai.brain.wordbase.verbs._assist import _ASSIST

#calss header
class _ASSISTED(_ASSIST, ):
	def __init__(self,): 
		_ASSIST.__init__(self)
		self.name = "ASSISTED"
		self.specie = 'verbs'
		self.basic = "assist"
		self.jsondata = {}
