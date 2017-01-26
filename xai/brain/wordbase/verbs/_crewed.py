

from xai.brain.wordbase.verbs._crew import _CREW

#calss header
class _CREWED(_CREW, ):
	def __init__(self,): 
		_CREW.__init__(self)
		self.name = "CREWED"
		self.specie = 'verbs'
		self.basic = "crew"
		self.jsondata = {}
