

from xai.brain.wordbase.nouns._crew import _CREW

#calss header
class _CREWED(_CREW, ):
	def __init__(self,): 
		_CREW.__init__(self)
		self.name = "CREWED"
		self.specie = 'nouns'
		self.basic = "crew"
		self.jsondata = {}
