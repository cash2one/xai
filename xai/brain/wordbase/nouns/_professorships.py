

from xai.brain.wordbase.nouns._professorship import _PROFESSORSHIP

#calss header
class _PROFESSORSHIPS(_PROFESSORSHIP, ):
	def __init__(self,): 
		_PROFESSORSHIP.__init__(self)
		self.name = "PROFESSORSHIPS"
		self.specie = 'nouns'
		self.basic = "professorship"
		self.jsondata = {}
