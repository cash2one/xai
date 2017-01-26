

from xai.brain.wordbase.verbs._motion import _MOTION

#calss header
class _MOTIONS(_MOTION, ):
	def __init__(self,): 
		_MOTION.__init__(self)
		self.name = "MOTIONS"
		self.specie = 'verbs'
		self.basic = "motion"
		self.jsondata = {}
