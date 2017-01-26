

from xai.brain.wordbase.verbs._vacuum import _VACUUM

#calss header
class _VACUUMED(_VACUUM, ):
	def __init__(self,): 
		_VACUUM.__init__(self)
		self.name = "VACUUMED"
		self.specie = 'verbs'
		self.basic = "vacuum"
		self.jsondata = {}
