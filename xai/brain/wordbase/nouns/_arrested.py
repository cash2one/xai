

from xai.brain.wordbase.nouns._arrest import _ARREST

#calss header
class _ARRESTED(_ARREST, ):
	def __init__(self,): 
		_ARREST.__init__(self)
		self.name = "ARRESTED"
		self.specie = 'nouns'
		self.basic = "arrest"
		self.jsondata = {}
