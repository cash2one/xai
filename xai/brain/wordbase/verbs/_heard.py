

from xai.brain.wordbase.verbs._hear import _HEAR

#calss header
class _HEARD(_HEAR, ):
	def __init__(self,): 
		_HEAR.__init__(self)
		self.name = "HEARD"
		self.specie = 'verbs'
		self.basic = "hear"
		self.jsondata = {}
