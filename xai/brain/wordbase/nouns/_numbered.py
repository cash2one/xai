

from xai.brain.wordbase.nouns._number import _NUMBER

#calss header
class _NUMBERED(_NUMBER, ):
	def __init__(self,): 
		_NUMBER.__init__(self)
		self.name = "NUMBERED"
		self.specie = 'nouns'
		self.basic = "number"
		self.jsondata = {}
