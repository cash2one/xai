

from xai.brain.wordbase.verbs._disagree import _DISAGREE

#calss header
class _DISAGREES(_DISAGREE, ):
	def __init__(self,): 
		_DISAGREE.__init__(self)
		self.name = "DISAGREES"
		self.specie = 'verbs'
		self.basic = "disagree"
		self.jsondata = {}
