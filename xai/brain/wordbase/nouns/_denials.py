

from xai.brain.wordbase.nouns._denial import _DENIAL

#calss header
class _DENIALS(_DENIAL, ):
	def __init__(self,): 
		_DENIAL.__init__(self)
		self.name = "DENIALS"
		self.specie = 'nouns'
		self.basic = "denial"
		self.jsondata = {}
