

from xai.brain.wordbase.nouns._politician import _POLITICIAN

#calss header
class _POLITICIANS(_POLITICIAN, ):
	def __init__(self,): 
		_POLITICIAN.__init__(self)
		self.name = "POLITICIANS"
		self.specie = 'nouns'
		self.basic = "politician"
		self.jsondata = {}
