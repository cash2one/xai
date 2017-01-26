

from xai.brain.wordbase.nouns._correlation import _CORRELATION

#calss header
class _CORRELATIONS(_CORRELATION, ):
	def __init__(self,): 
		_CORRELATION.__init__(self)
		self.name = "CORRELATIONS"
		self.specie = 'nouns'
		self.basic = "correlation"
		self.jsondata = {}
