

from xai.brain.wordbase.nouns._registration import _REGISTRATION

#calss header
class _REGISTRATIONS(_REGISTRATION, ):
	def __init__(self,): 
		_REGISTRATION.__init__(self)
		self.name = "REGISTRATIONS"
		self.specie = 'nouns'
		self.basic = "registration"
		self.jsondata = {}
