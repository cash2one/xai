

from xai.brain.wordbase.nouns._affix import _AFFIX

#calss header
class _AFFIXED(_AFFIX, ):
	def __init__(self,): 
		_AFFIX.__init__(self)
		self.name = "AFFIXED"
		self.specie = 'nouns'
		self.basic = "affix"
		self.jsondata = {}
