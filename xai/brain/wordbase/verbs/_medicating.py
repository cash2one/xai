

from xai.brain.wordbase.verbs._medicate import _MEDICATE

#calss header
class _MEDICATING(_MEDICATE, ):
	def __init__(self,): 
		_MEDICATE.__init__(self)
		self.name = "MEDICATING"
		self.specie = 'verbs'
		self.basic = "medicate"
		self.jsondata = {}
