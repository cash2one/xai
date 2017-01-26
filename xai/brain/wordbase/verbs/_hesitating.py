

from xai.brain.wordbase.verbs._hesitate import _HESITATE

#calss header
class _HESITATING(_HESITATE, ):
	def __init__(self,): 
		_HESITATE.__init__(self)
		self.name = "HESITATING"
		self.specie = 'verbs'
		self.basic = "hesitate"
		self.jsondata = {}
