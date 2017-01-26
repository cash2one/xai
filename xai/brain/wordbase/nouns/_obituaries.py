

from xai.brain.wordbase.nouns._obituary import _OBITUARY

#calss header
class _OBITUARIES(_OBITUARY, ):
	def __init__(self,): 
		_OBITUARY.__init__(self)
		self.name = "OBITUARIES"
		self.specie = 'nouns'
		self.basic = "obituary"
		self.jsondata = {}
