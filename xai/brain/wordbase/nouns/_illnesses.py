

from xai.brain.wordbase.nouns._illness import _ILLNESS

#calss header
class _ILLNESSES(_ILLNESS, ):
	def __init__(self,): 
		_ILLNESS.__init__(self)
		self.name = "ILLNESSES"
		self.specie = 'nouns'
		self.basic = "illness"
		self.jsondata = {}
