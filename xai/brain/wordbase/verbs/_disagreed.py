

from xai.brain.wordbase.verbs._disagree import _DISAGREE

#calss header
class _DISAGREED(_DISAGREE, ):
	def __init__(self,): 
		_DISAGREE.__init__(self)
		self.name = "DISAGREED"
		self.specie = 'verbs'
		self.basic = "disagree"
		self.jsondata = {}
