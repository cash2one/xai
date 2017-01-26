

from xai.brain.wordbase.nouns._filing import _FILING

#calss header
class _FILINGS(_FILING, ):
	def __init__(self,): 
		_FILING.__init__(self)
		self.name = "FILINGS"
		self.specie = 'nouns'
		self.basic = "filing"
		self.jsondata = {}
