

from xai.brain.wordbase.verbs._perceive import _PERCEIVE

#calss header
class _PERCEIVED(_PERCEIVE, ):
	def __init__(self,): 
		_PERCEIVE.__init__(self)
		self.name = "PERCEIVED"
		self.specie = 'verbs'
		self.basic = "perceive"
		self.jsondata = {}
