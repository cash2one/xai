

from xai.brain.wordbase.verbs._patent import _PATENT

#calss header
class _PATENTING(_PATENT, ):
	def __init__(self,): 
		_PATENT.__init__(self)
		self.name = "PATENTING"
		self.specie = 'verbs'
		self.basic = "patent"
		self.jsondata = {}
