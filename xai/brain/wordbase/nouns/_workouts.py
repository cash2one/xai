

from xai.brain.wordbase.nouns._workout import _WORKOUT

#calss header
class _WORKOUTS(_WORKOUT, ):
	def __init__(self,): 
		_WORKOUT.__init__(self)
		self.name = "WORKOUTS"
		self.specie = 'nouns'
		self.basic = "workout"
		self.jsondata = {}
