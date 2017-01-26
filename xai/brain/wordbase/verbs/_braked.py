

from xai.brain.wordbase.verbs._brake import _BRAKE

#calss header
class _BRAKED(_BRAKE, ):
	def __init__(self,): 
		_BRAKE.__init__(self)
		self.name = "BRAKED"
		self.specie = 'verbs'
		self.basic = "brake"
		self.jsondata = {}
