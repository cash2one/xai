

from xai.brain.wordbase.verbs._disapprove import _DISAPPROVE

#calss header
class _DISAPPROVED(_DISAPPROVE, ):
	def __init__(self,): 
		_DISAPPROVE.__init__(self)
		self.name = "DISAPPROVED"
		self.specie = 'verbs'
		self.basic = "disapprove"
		self.jsondata = {}
