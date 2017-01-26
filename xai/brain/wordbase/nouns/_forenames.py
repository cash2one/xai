

from xai.brain.wordbase.nouns._forename import _FORENAME

#calss header
class _FORENAMES(_FORENAME, ):
	def __init__(self,): 
		_FORENAME.__init__(self)
		self.name = "FORENAMES"
		self.specie = 'nouns'
		self.basic = "forename"
		self.jsondata = {}
