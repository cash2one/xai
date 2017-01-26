

from xai.brain.wordbase.verbs._sift import _SIFT

#calss header
class _SIFTED(_SIFT, ):
	def __init__(self,): 
		_SIFT.__init__(self)
		self.name = "SIFTED"
		self.specie = 'verbs'
		self.basic = "sift"
		self.jsondata = {}
