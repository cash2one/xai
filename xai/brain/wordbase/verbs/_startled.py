

from xai.brain.wordbase.verbs._startle import _STARTLE

#calss header
class _STARTLED(_STARTLE, ):
	def __init__(self,): 
		_STARTLE.__init__(self)
		self.name = "STARTLED"
		self.specie = 'verbs'
		self.basic = "startle"
		self.jsondata = {}
