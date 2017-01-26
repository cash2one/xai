

from xai.brain.wordbase.nouns._employment import _EMPLOYMENT

#calss header
class _EMPLOYMENTS(_EMPLOYMENT, ):
	def __init__(self,): 
		_EMPLOYMENT.__init__(self)
		self.name = "EMPLOYMENTS"
		self.specie = 'nouns'
		self.basic = "employment"
		self.jsondata = {}
