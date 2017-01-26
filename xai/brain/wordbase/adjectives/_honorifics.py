

from xai.brain.wordbase.adjectives._honorific import _HONORIFIC

#calss header
class _HONORIFICS(_HONORIFIC, ):
	def __init__(self,): 
		_HONORIFIC.__init__(self)
		self.name = "HONORIFICS"
		self.specie = 'adjectives'
		self.basic = "honorific"
		self.jsondata = {}
