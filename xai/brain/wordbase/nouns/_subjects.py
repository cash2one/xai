

from xai.brain.wordbase.nouns._subject import _SUBJECT

#calss header
class _SUBJECTS(_SUBJECT, ):
	def __init__(self,): 
		_SUBJECT.__init__(self)
		self.name = "SUBJECTS"
		self.specie = 'nouns'
		self.basic = "subject"
		self.jsondata = {}
