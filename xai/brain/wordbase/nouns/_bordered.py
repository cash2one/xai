

from xai.brain.wordbase.nouns._border import _BORDER

#calss header
class _BORDERED(_BORDER, ):
	def __init__(self,): 
		_BORDER.__init__(self)
		self.name = "BORDERED"
		self.specie = 'nouns'
		self.basic = "border"
		self.jsondata = {}
