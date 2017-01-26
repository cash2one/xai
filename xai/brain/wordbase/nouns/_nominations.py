

from xai.brain.wordbase.nouns._nomination import _NOMINATION

#calss header
class _NOMINATIONS(_NOMINATION, ):
	def __init__(self,): 
		_NOMINATION.__init__(self)
		self.name = "NOMINATIONS"
		self.specie = 'nouns'
		self.basic = "nomination"
		self.jsondata = {}
