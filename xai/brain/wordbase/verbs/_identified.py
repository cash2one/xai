

from xai.brain.wordbase.verbs._identify import _IDENTIFY

#calss header
class _IDENTIFIED(_IDENTIFY, ):
	def __init__(self,): 
		_IDENTIFY.__init__(self)
		self.name = "IDENTIFIED"
		self.specie = 'verbs'
		self.basic = "identify"
		self.jsondata = {}
