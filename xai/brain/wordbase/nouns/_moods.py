

from xai.brain.wordbase.nouns._mood import _MOOD

#calss header
class _MOODS(_MOOD, ):
	def __init__(self,): 
		_MOOD.__init__(self)
		self.name = "MOODS"
		self.specie = 'nouns'
		self.basic = "mood"
		self.jsondata = {}
