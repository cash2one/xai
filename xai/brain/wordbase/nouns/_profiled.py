

from xai.brain.wordbase.nouns._profile import _PROFILE

#calss header
class _PROFILED(_PROFILE, ):
	def __init__(self,): 
		_PROFILE.__init__(self)
		self.name = "PROFILED"
		self.specie = 'nouns'
		self.basic = "profile"
		self.jsondata = {}
