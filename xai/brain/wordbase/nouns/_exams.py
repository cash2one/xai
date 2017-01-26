

from xai.brain.wordbase.nouns._exam import _EXAM

#calss header
class _EXAMS(_EXAM, ):
	def __init__(self,): 
		_EXAM.__init__(self)
		self.name = "EXAMS"
		self.specie = 'nouns'
		self.basic = "exam"
		self.jsondata = {}
