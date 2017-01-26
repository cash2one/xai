

from xai.brain.wordbase.verbs._disagree import _DISAGREE

#calss header
class _DISAGREEING(_DISAGREE, ):
	def __init__(self,): 
		_DISAGREE.__init__(self)
		self.name = "DISAGREEING"
		self.specie = 'verbs'
		self.basic = "disagree"
		self.jsondata = {}
