

from xai.brain.wordbase.nouns._reject import _REJECT

#calss header
class _REJECTED(_REJECT, ):
	def __init__(self,): 
		_REJECT.__init__(self)
		self.name = "REJECTED"
		self.specie = 'nouns'
		self.basic = "reject"
		self.jsondata = {}
