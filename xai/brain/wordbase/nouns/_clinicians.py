

from xai.brain.wordbase.nouns._clinician import _CLINICIAN

#calss header
class _CLINICIANS(_CLINICIAN, ):
	def __init__(self,): 
		_CLINICIAN.__init__(self)
		self.name = "CLINICIANS"
		self.specie = 'nouns'
		self.basic = "clinician"
		self.jsondata = {}
