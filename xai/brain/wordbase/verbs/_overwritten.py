

from xai.brain.wordbase.verbs._overwrite import _OVERWRITE

#calss header
class _OVERWRITTEN(_OVERWRITE, ):
	def __init__(self,): 
		_OVERWRITE.__init__(self)
		self.name = "OVERWRITTEN"
		self.specie = 'verbs'
		self.basic = "overwrite"
		self.jsondata = {}
