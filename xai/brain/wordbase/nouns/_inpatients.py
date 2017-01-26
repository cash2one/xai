

from xai.brain.wordbase.nouns._inpatient import _INPATIENT

#calss header
class _INPATIENTS(_INPATIENT, ):
	def __init__(self,): 
		_INPATIENT.__init__(self)
		self.name = "INPATIENTS"
		self.specie = 'nouns'
		self.basic = "inpatient"
		self.jsondata = {}
