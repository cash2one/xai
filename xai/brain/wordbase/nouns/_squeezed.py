

from xai.brain.wordbase.nouns._squeeze import _SQUEEZE

#calss header
class _SQUEEZED(_SQUEEZE, ):
	def __init__(self,): 
		_SQUEEZE.__init__(self)
		self.name = "SQUEEZED"
		self.specie = 'nouns'
		self.basic = "squeeze"
		self.jsondata = {}
