

from xai.brain.wordbase.nouns._patient import _PATIENT

#calss header
class _PATIENTS(_PATIENT, ):
	def __init__(self,): 
		_PATIENT.__init__(self)
		self.name = "PATIENTS"
		self.specie = 'nouns'
		self.basic = "patient"
		self.jsondata = {}
