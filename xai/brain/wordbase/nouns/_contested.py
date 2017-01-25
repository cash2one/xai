

from xai.brain.wordbase.nouns._contest import _CONTEST

#calss header
class _CONTESTED(_CONTEST, ):
	def __init__(self,): 
		_CONTEST.__init__(self)
		self.name = "CONTESTED"
		self.specie = 'nouns'
		self.basic = "contest"
		self.jsondata = {}
