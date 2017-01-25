

from xai.brain.wordbase.verbs._caption import _CAPTION

#calss header
class _CAPTIONED(_CAPTION, ):
	def __init__(self,): 
		_CAPTION.__init__(self)
		self.name = "CAPTIONED"
		self.specie = 'verbs'
		self.basic = "caption"
		self.jsondata = {}
