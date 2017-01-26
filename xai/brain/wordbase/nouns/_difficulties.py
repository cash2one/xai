

from xai.brain.wordbase.nouns._difficulty import _DIFFICULTY

#calss header
class _DIFFICULTIES(_DIFFICULTY, ):
	def __init__(self,): 
		_DIFFICULTY.__init__(self)
		self.name = "DIFFICULTIES"
		self.specie = 'nouns'
		self.basic = "difficulty"
		self.jsondata = {}
