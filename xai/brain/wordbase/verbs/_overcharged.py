

from xai.brain.wordbase.verbs._overcharge import _OVERCHARGE

#calss header
class _OVERCHARGED(_OVERCHARGE, ):
	def __init__(self,): 
		_OVERCHARGE.__init__(self)
		self.name = "OVERCHARGED"
		self.specie = 'verbs'
		self.basic = "overcharge"
		self.jsondata = {}
