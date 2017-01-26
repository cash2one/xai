

from xai.brain.wordbase.nouns._laureate import _LAUREATE

#calss header
class _LAUREATES(_LAUREATE, ):
	def __init__(self,): 
		_LAUREATE.__init__(self)
		self.name = "LAUREATES"
		self.specie = 'nouns'
		self.basic = "laureate"
		self.jsondata = {}
