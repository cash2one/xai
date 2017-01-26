

from xai.brain.wordbase.nouns._fortune import _FORTUNE

#calss header
class _FORTUNES(_FORTUNE, ):
	def __init__(self,): 
		_FORTUNE.__init__(self)
		self.name = "FORTUNES"
		self.specie = 'nouns'
		self.basic = "fortune"
		self.jsondata = {}
