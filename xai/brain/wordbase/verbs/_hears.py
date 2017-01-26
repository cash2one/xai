

from xai.brain.wordbase.verbs._hear import _HEAR

#calss header
class _HEARS(_HEAR, ):
	def __init__(self,): 
		_HEAR.__init__(self)
		self.name = "HEARS"
		self.specie = 'verbs'
		self.basic = "hear"
		self.jsondata = {}
