

from xai.brain.wordbase.adjectives._patent import _PATENT

#calss header
class _PATENTED(_PATENT, ):
	def __init__(self,): 
		_PATENT.__init__(self)
		self.name = "PATENTED"
		self.specie = 'adjectives'
		self.basic = "patent"
		self.jsondata = {}
