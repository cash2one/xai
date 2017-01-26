

from xai.brain.wordbase.verbs._forswear import _FORSWEAR

#calss header
class _FORSWORN(_FORSWEAR, ):
	def __init__(self,): 
		_FORSWEAR.__init__(self)
		self.name = "FORSWORN"
		self.specie = 'verbs'
		self.basic = "forswear"
		self.jsondata = {}
