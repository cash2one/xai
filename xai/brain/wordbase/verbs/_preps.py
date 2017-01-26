

from xai.brain.wordbase.verbs._prep import _PREP

#calss header
class _PREPS(_PREP, ):
	def __init__(self,): 
		_PREP.__init__(self)
		self.name = "PREPS"
		self.specie = 'verbs'
		self.basic = "prep"
		self.jsondata = {}
