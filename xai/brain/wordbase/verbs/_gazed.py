

from xai.brain.wordbase.verbs._gaze import _GAZE

#calss header
class _GAZED(_GAZE, ):
	def __init__(self,): 
		_GAZE.__init__(self)
		self.name = "GAZED"
		self.specie = 'verbs'
		self.basic = "gaze"
		self.jsondata = {}
