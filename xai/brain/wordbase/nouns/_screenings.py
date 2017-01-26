

from xai.brain.wordbase.nouns._screening import _SCREENING

#calss header
class _SCREENINGS(_SCREENING, ):
	def __init__(self,): 
		_SCREENING.__init__(self)
		self.name = "SCREENINGS"
		self.specie = 'nouns'
		self.basic = "screening"
		self.jsondata = {}
