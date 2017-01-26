

from xai.brain.wordbase.nouns._grade import _GRADE

#calss header
class _GRADED(_GRADE, ):
	def __init__(self,): 
		_GRADE.__init__(self)
		self.name = "GRADED"
		self.specie = 'nouns'
		self.basic = "grade"
		self.jsondata = {}
