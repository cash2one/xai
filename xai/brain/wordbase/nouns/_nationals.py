

from xai.brain.wordbase.nouns._national import _NATIONAL

#calss header
class _NATIONALS(_NATIONAL, ):
	def __init__(self,): 
		_NATIONAL.__init__(self)
		self.name = "NATIONALS"
		self.specie = 'nouns'
		self.basic = "national"
		self.jsondata = {}
