

from xai.brain.wordbase.adjectives._patient import _PATIENT

#calss header
class _PATIENTS(_PATIENT, ):
	def __init__(self,): 
		_PATIENT.__init__(self)
		self.name = "PATIENTS"
		self.specie = 'adjectives'
		self.basic = "patient"
		self.jsondata = {}
