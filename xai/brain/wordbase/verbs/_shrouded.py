

from xai.brain.wordbase.verbs._shroud import _SHROUD

#calss header
class _SHROUDED(_SHROUD, ):
	def __init__(self,): 
		_SHROUD.__init__(self)
		self.name = "SHROUDED"
		self.specie = 'verbs'
		self.basic = "shroud"
		self.jsondata = {}
