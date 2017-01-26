

from xai.brain.wordbase.nouns._reject import _REJECT

#calss header
class _REJECTS(_REJECT, ):
	def __init__(self,): 
		_REJECT.__init__(self)
		self.name = "REJECTS"
		self.specie = 'nouns'
		self.basic = "reject"
		self.jsondata = {}
