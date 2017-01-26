

from xai.brain.wordbase.verbs._border import _BORDER

#calss header
class _BORDERED(_BORDER, ):
	def __init__(self,): 
		_BORDER.__init__(self)
		self.name = "BORDERED"
		self.specie = 'verbs'
		self.basic = "border"
		self.jsondata = {}
