

from xai.brain.wordbase.nouns._motion import _MOTION

#calss header
class _MOTIONS(_MOTION, ):
	def __init__(self,): 
		_MOTION.__init__(self)
		self.name = "MOTIONS"
		self.specie = 'nouns'
		self.basic = "motion"
		self.jsondata = {}
