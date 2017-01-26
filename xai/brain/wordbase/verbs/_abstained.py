

from xai.brain.wordbase.verbs._abstain import _ABSTAIN

#calss header
class _ABSTAINED(_ABSTAIN, ):
	def __init__(self,): 
		_ABSTAIN.__init__(self)
		self.name = "ABSTAINED"
		self.specie = 'verbs'
		self.basic = "abstain"
		self.jsondata = {}
