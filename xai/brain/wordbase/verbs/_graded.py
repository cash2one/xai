

from xai.brain.wordbase.verbs._grade import _GRADE

#calss header
class _GRADED(_GRADE, ):
	def __init__(self,): 
		_GRADE.__init__(self)
		self.name = "GRADED"
		self.specie = 'verbs'
		self.basic = "grade"
		self.jsondata = {}
