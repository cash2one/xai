

from xai.brain.wordbase.verbs._blackball import _BLACKBALL

#calss header
class _BLACKBALLED(_BLACKBALL, ):
	def __init__(self,): 
		_BLACKBALL.__init__(self)
		self.name = "BLACKBALLED"
		self.specie = 'verbs'
		self.basic = "blackball"
		self.jsondata = {}
