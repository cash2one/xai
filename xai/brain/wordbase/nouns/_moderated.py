

from xai.brain.wordbase.nouns._moderate import _MODERATE

#calss header
class _MODERATED(_MODERATE, ):
	def __init__(self,): 
		_MODERATE.__init__(self)
		self.name = "MODERATED"
		self.specie = 'nouns'
		self.basic = "moderate"
		self.jsondata = {}
