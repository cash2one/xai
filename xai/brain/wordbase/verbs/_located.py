

from xai.brain.wordbase.verbs._locate import _LOCATE

#calss header
class _LOCATED(_LOCATE, ):
	def __init__(self,): 
		_LOCATE.__init__(self)
		self.name = "LOCATED"
		self.specie = 'verbs'
		self.basic = "locate"
		self.jsondata = {}
