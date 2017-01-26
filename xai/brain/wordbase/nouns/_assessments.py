

from xai.brain.wordbase.nouns._assessment import _ASSESSMENT

#calss header
class _ASSESSMENTS(_ASSESSMENT, ):
	def __init__(self,): 
		_ASSESSMENT.__init__(self)
		self.name = "ASSESSMENTS"
		self.specie = 'nouns'
		self.basic = "assessment"
		self.jsondata = {}
