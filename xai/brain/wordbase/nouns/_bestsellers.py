

from xai.brain.wordbase.nouns._bestseller import _BESTSELLER

#calss header
class _BESTSELLERS(_BESTSELLER, ):
	def __init__(self,): 
		_BESTSELLER.__init__(self)
		self.name = "BESTSELLERS"
		self.specie = 'nouns'
		self.basic = "bestseller"
		self.jsondata = {}
