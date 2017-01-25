

from xai.brain.wordbase.nouns._attendance import _ATTENDANCE

#calss header
class _ATTENDANCES(_ATTENDANCE, ):
	def __init__(self,): 
		_ATTENDANCE.__init__(self)
		self.name = "ATTENDANCES"
		self.specie = 'nouns'
		self.basic = "attendance"
		self.jsondata = {}
