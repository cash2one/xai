

from xai.brain.wordbase.verbs._perceive import _PERCEIVE

#calss header
class _PERCEIVES(_PERCEIVE, ):
	def __init__(self,): 
		_PERCEIVE.__init__(self)
		self.name = "PERCEIVES"
		self.specie = 'verbs'
		self.basic = "perceive"
		self.jsondata = {}
