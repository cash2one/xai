

from xai.brain.wordbase.nouns._examination import _EXAMINATION

#calss header
class _EXAMINATIONS(_EXAMINATION, ):
	def __init__(self,): 
		_EXAMINATION.__init__(self)
		self.name = "EXAMINATIONS"
		self.specie = 'nouns'
		self.basic = "examination"
		self.jsondata = {}
