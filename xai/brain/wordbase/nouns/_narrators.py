

from xai.brain.wordbase.nouns._narrator import _NARRATOR

#calss header
class _NARRATORS(_NARRATOR, ):
	def __init__(self,): 
		_NARRATOR.__init__(self)
		self.name = "NARRATORS"
		self.specie = 'nouns'
		self.basic = "narrator"
		self.jsondata = {}
