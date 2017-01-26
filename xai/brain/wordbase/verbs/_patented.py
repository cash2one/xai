

from xai.brain.wordbase.verbs._patent import _PATENT

#calss header
class _PATENTED(_PATENT, ):
	def __init__(self,): 
		_PATENT.__init__(self)
		self.name = "PATENTED"
		self.specie = 'verbs'
		self.basic = "patent"
		self.jsondata = {}
