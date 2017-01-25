

from xai.brain.wordbase.nouns._caption import _CAPTION

#calss header
class _CAPTIONED(_CAPTION, ):
	def __init__(self,): 
		_CAPTION.__init__(self)
		self.name = "CAPTIONED"
		self.specie = 'nouns'
		self.basic = "caption"
		self.jsondata = {}
