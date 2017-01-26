

from xai.brain.wordbase.nouns._loss import _LOSS

#calss header
class _LOSSES(_LOSS, ):
	def __init__(self,): 
		_LOSS.__init__(self)
		self.name = "LOSSES"
		self.specie = 'nouns'
		self.basic = "loss"
		self.jsondata = {}
