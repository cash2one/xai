

from xai.brain.wordbase.verbs._jail import _JAIL

#calss header
class _JAILED(_JAIL, ):
	def __init__(self,): 
		_JAIL.__init__(self)
		self.name = "JAILED"
		self.specie = 'verbs'
		self.basic = "jail"
		self.jsondata = {}
