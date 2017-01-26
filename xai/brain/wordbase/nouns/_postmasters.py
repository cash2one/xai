

from xai.brain.wordbase.nouns._postmaster import _POSTMASTER

#calss header
class _POSTMASTERS(_POSTMASTER, ):
	def __init__(self,): 
		_POSTMASTER.__init__(self)
		self.name = "POSTMASTERS"
		self.specie = 'nouns'
		self.basic = "postmaster"
		self.jsondata = {}
