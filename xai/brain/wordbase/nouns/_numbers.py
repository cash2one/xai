

from xai.brain.wordbase.nouns._number import _NUMBER

#calss header
class _NUMBERS(_NUMBER, ):
	def __init__(self,): 
		_NUMBER.__init__(self)
		self.name = "NUMBERS"
		self.specie = 'nouns'
		self.basic = "number"
		self.jsondata = {}
