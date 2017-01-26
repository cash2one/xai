

from xai.brain.wordbase.verbs._detain import _DETAIN

#calss header
class _DETAINED(_DETAIN, ):
	def __init__(self,): 
		_DETAIN.__init__(self)
		self.name = "DETAINED"
		self.specie = 'verbs'
		self.basic = "detain"
		self.jsondata = {}
