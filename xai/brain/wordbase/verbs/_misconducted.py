

from xai.brain.wordbase.verbs._misconduct import _MISCONDUCT

#calss header
class _MISCONDUCTED(_MISCONDUCT, ):
	def __init__(self,): 
		_MISCONDUCT.__init__(self)
		self.name = "MISCONDUCTED"
		self.specie = 'verbs'
		self.basic = "misconduct"
		self.jsondata = {}
