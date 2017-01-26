

from xai.brain.wordbase.verbs._affix import _AFFIX

#calss header
class _AFFIXED(_AFFIX, ):
	def __init__(self,): 
		_AFFIX.__init__(self)
		self.name = "AFFIXED"
		self.specie = 'verbs'
		self.basic = "affix"
		self.jsondata = {}
