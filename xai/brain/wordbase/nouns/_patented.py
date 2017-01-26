

from xai.brain.wordbase.nouns._patent import _PATENT

#calss header
class _PATENTED(_PATENT, ):
	def __init__(self,): 
		_PATENT.__init__(self)
		self.name = "PATENTED"
		self.specie = 'nouns'
		self.basic = "patent"
		self.jsondata = {}
