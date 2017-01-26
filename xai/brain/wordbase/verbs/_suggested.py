

from xai.brain.wordbase.verbs._suggest import _SUGGEST

#calss header
class _SUGGESTED(_SUGGEST, ):
	def __init__(self,): 
		_SUGGEST.__init__(self)
		self.name = "SUGGESTED"
		self.specie = 'verbs'
		self.basic = "suggest"
		self.jsondata = {}
