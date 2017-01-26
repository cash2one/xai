

from xai.brain.wordbase.adjectives._sick import _SICK

#calss header
class _SICKER(_SICK, ):
	def __init__(self,): 
		_SICK.__init__(self)
		self.name = "SICKER"
		self.specie = 'adjectives'
		self.basic = "sick"
		self.jsondata = {}
