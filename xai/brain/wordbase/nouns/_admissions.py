

from xai.brain.wordbase.nouns._admission import _ADMISSION

#calss header
class _ADMISSIONS(_ADMISSION, ):
	def __init__(self,): 
		_ADMISSION.__init__(self)
		self.name = "ADMISSIONS"
		self.specie = 'nouns'
		self.basic = "admission"
		self.jsondata = {}
