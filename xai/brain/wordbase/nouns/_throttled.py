

from xai.brain.wordbase.nouns._throttle import _THROTTLE

#calss header
class _THROTTLED(_THROTTLE, ):
	def __init__(self,): 
		_THROTTLE.__init__(self)
		self.name = "THROTTLED"
		self.specie = 'nouns'
		self.basic = "throttle"
		self.jsondata = {}
