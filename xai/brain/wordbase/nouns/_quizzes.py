

from xai.brain.wordbase.nouns._quiz import _QUIZ

#calss header
class _QUIZZES(_QUIZ, ):
	def __init__(self,): 
		_QUIZ.__init__(self)
		self.name = "QUIZZES"
		self.specie = 'nouns'
		self.basic = "quiz"
		self.jsondata = {}
