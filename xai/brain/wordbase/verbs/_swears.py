

from xai.brain.wordbase.verbs._swear import _SWEAR

#calss header
class _SWEARS(_SWEAR, ):
	def __init__(self,): 
		_SWEAR.__init__(self)
		self.name = "SWEARS"
		self.specie = 'verbs'
		self.basic = "swear"
		self.jsondata = {}
