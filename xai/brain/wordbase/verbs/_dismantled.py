

from xai.brain.wordbase.verbs._dismantle import _DISMANTLE

#calss header
class _DISMANTLED(_DISMANTLE, ):
	def __init__(self,): 
		_DISMANTLE.__init__(self)
		self.name = "DISMANTLED"
		self.specie = 'verbs'
		self.basic = "dismantle"
		self.jsondata = {}
