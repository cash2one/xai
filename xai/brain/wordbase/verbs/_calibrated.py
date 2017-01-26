

from xai.brain.wordbase.verbs._calibrate import _CALIBRATE

#calss header
class _CALIBRATED(_CALIBRATE, ):
	def __init__(self,): 
		_CALIBRATE.__init__(self)
		self.name = "CALIBRATED"
		self.specie = 'verbs'
		self.basic = "calibrate"
		self.jsondata = {}
