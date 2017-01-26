

from xai.brain.wordbase.nouns._company import _COMPANY

#calss header
class _COMPANIES(_COMPANY, ):
	def __init__(self,): 
		_COMPANY.__init__(self)
		self.name = "COMPANIES"
		self.specie = 'nouns'
		self.basic = "company"
		self.jsondata = {}
