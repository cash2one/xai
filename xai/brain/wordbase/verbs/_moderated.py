

from xai.brain.wordbase.verbs._moderate import _MODERATE

#calss header
class _MODERATED(_MODERATE, ):
	def __init__(self,): 
		_MODERATE.__init__(self)
		self.name = "MODERATED"
		self.specie = 'verbs'
		self.basic = "moderate"
		self.jsondata = {}
