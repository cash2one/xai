

from xai.brain.wordbase.nouns._living import _LIVING

#calss header
class _LIVINGS(_LIVING, ):
	def __init__(self,): 
		_LIVING.__init__(self)
		self.name = "LIVINGS"
		self.specie = 'nouns'
		self.basic = "living"
		self.jsondata = {}
