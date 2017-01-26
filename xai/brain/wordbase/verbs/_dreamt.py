

from xai.brain.wordbase.verbs._dream import _DREAM

#calss header
class _DREAMT(_DREAM, ):
	def __init__(self,): 
		_DREAM.__init__(self)
		self.name = "DREAMT"
		self.specie = 'verbs'
		self.basic = "dream"
		self.jsondata = {}
