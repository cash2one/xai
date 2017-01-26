

from xai.brain.wordbase.verbs._refuse import _REFUSE

#calss header
class _REFUSED(_REFUSE, ):
	def __init__(self,): 
		_REFUSE.__init__(self)
		self.name = "REFUSED"
		self.specie = 'verbs'
		self.basic = "refuse"
		self.jsondata = {}
