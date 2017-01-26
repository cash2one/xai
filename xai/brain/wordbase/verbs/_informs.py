

from xai.brain.wordbase.verbs._inform import _INFORM

#calss header
class _INFORMS(_INFORM, ):
	def __init__(self,): 
		_INFORM.__init__(self)
		self.name = "INFORMS"
		self.specie = 'verbs'
		self.basic = "inform"
		self.jsondata = {}
