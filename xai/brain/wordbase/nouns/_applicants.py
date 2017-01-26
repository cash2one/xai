

from xai.brain.wordbase.nouns._applicant import _APPLICANT

#calss header
class _APPLICANTS(_APPLICANT, ):
	def __init__(self,): 
		_APPLICANT.__init__(self)
		self.name = "APPLICANTS"
		self.specie = 'nouns'
		self.basic = "applicant"
		self.jsondata = {}
