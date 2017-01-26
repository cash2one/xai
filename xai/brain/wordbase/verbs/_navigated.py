

from xai.brain.wordbase.verbs._navigate import _NAVIGATE

#calss header
class _NAVIGATED(_NAVIGATE, ):
	def __init__(self,): 
		_NAVIGATE.__init__(self)
		self.name = "NAVIGATED"
		self.specie = 'verbs'
		self.basic = "navigate"
		self.jsondata = {}
