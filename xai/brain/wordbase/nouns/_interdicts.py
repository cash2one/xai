

from xai.brain.wordbase.nouns._interdict import _INTERDICT

#calss header
class _INTERDICTS(_INTERDICT, ):
	def __init__(self,): 
		_INTERDICT.__init__(self)
		self.name = "INTERDICTS"
		self.specie = 'nouns'
		self.basic = "interdict"
		self.jsondata = {}
