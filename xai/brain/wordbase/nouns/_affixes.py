

from xai.brain.wordbase.nouns._affix import _AFFIX

#calss header
class _AFFIXES(_AFFIX, ):
	def __init__(self,): 
		_AFFIX.__init__(self)
		self.name = "AFFIXES"
		self.specie = 'nouns'
		self.basic = "affix"
		self.jsondata = {}
