

from xai.brain.wordbase.verbs._imply import _IMPLY

#calss header
class _IMPLIES(_IMPLY, ):
	def __init__(self,): 
		_IMPLY.__init__(self)
		self.name = "IMPLIES"
		self.specie = 'verbs'
		self.basic = "imply"
		self.jsondata = {}
