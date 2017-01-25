

from xai.brain.wordbase.verbs._heal import _HEAL

#calss header
class _HEALED(_HEAL, ):
	def __init__(self,): 
		_HEAL.__init__(self)
		self.name = "HEALED"
		self.specie = 'verbs'
		self.basic = "heal"
		self.jsondata = {}
