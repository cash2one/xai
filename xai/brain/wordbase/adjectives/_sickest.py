

from xai.brain.wordbase.adjectives._sick import _SICK

#calss header
class _SICKEST(_SICK, ):
	def __init__(self,): 
		_SICK.__init__(self)
		self.name = "SICKEST"
		self.specie = 'adjectives'
		self.basic = "sick"
		self.jsondata = {}
