

from xai.brain.wordbase.nouns._faculty import _FACULTY

#calss header
class _FACULTIES(_FACULTY, ):
	def __init__(self,): 
		_FACULTY.__init__(self)
		self.name = "FACULTIES"
		self.specie = 'nouns'
		self.basic = "faculty"
		self.jsondata = {}
