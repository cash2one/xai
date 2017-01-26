

from xai.brain.wordbase.nouns._caption import _CAPTION

#calss header
class _CAPTIONS(_CAPTION, ):
	def __init__(self,): 
		_CAPTION.__init__(self)
		self.name = "CAPTIONS"
		self.specie = 'nouns'
		self.basic = "caption"
		self.jsondata = {}
