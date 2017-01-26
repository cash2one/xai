

from xai.brain.wordbase.verbs._persuade import _PERSUADE

#calss header
class _PERSUADED(_PERSUADE, ):
	def __init__(self,): 
		_PERSUADE.__init__(self)
		self.name = "PERSUADED"
		self.specie = 'verbs'
		self.basic = "persuade"
		self.jsondata = {}
