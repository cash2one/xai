

from xai.brain.wordbase.nouns._holdout import _HOLDOUT

#calss header
class _HOLDOUTS(_HOLDOUT, ):
	def __init__(self,): 
		_HOLDOUT.__init__(self)
		self.name = "HOLDOUTS"
		self.specie = 'nouns'
		self.basic = "holdout"
		self.jsondata = {}
