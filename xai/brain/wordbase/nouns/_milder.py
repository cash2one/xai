

from xai.brain.wordbase.nouns._mild import _MILD

#calss header
class _MILDER(_MILD, ):
	def __init__(self,): 
		_MILD.__init__(self)
		self.name = "MILDER"
		self.specie = 'nouns'
		self.basic = "mild"
		self.jsondata = {}
