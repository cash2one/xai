

from xai.brain.wordbase.nouns._complaint import _COMPLAINT

#calss header
class _COMPLAINTS(_COMPLAINT, ):
	def __init__(self,): 
		_COMPLAINT.__init__(self)
		self.name = "COMPLAINTS"
		self.specie = 'nouns'
		self.basic = "complaint"
		self.jsondata = {}
