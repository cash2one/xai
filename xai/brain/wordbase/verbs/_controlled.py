

from xai.brain.wordbase.verbs._control import _CONTROL

#calss header
class _CONTROLLED(_CONTROL, ):
	def __init__(self,): 
		_CONTROL.__init__(self)
		self.name = "CONTROLLED"
		self.specie = 'verbs'
		self.basic = "control"
		self.jsondata = {}
