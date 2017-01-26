

from xai.brain.wordbase.nouns._instrument import _INSTRUMENT

#calss header
class _INSTRUMENTED(_INSTRUMENT, ):
	def __init__(self,): 
		_INSTRUMENT.__init__(self)
		self.name = "INSTRUMENTED"
		self.specie = 'nouns'
		self.basic = "instrument"
		self.jsondata = {}
