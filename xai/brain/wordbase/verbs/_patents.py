

from xai.brain.wordbase.verbs._patent import _PATENT

#calss header
class _PATENTS(_PATENT, ):
	def __init__(self,): 
		_PATENT.__init__(self)
		self.name = "PATENTS"
		self.specie = 'verbs'
		self.basic = "patent"
		self.jsondata = {}
