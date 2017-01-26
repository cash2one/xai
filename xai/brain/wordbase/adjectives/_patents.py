

from xai.brain.wordbase.adjectives._patent import _PATENT

#calss header
class _PATENTS(_PATENT, ):
	def __init__(self,): 
		_PATENT.__init__(self)
		self.name = "PATENTS"
		self.specie = 'adjectives'
		self.basic = "patent"
		self.jsondata = {}
