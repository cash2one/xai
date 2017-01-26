

from xai.brain.wordbase.verbs._demean import _DEMEAN

#calss header
class _DEMEANED(_DEMEAN, ):
	def __init__(self,): 
		_DEMEAN.__init__(self)
		self.name = "DEMEANED"
		self.specie = 'verbs'
		self.basic = "demean"
		self.jsondata = {}
