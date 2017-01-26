

from xai.brain.wordbase.nouns._sum import _SUM

#calss header
class _SUMMED(_SUM, ):
	def __init__(self,): 
		_SUM.__init__(self)
		self.name = "SUMMED"
		self.specie = 'nouns'
		self.basic = "sum"
		self.jsondata = {}
