

from xai.brain.wordbase.verbs._subscribe import _SUBSCRIBE

#calss header
class _SUBSCRIBED(_SUBSCRIBE, ):
	def __init__(self,): 
		_SUBSCRIBE.__init__(self)
		self.name = "SUBSCRIBED"
		self.specie = 'verbs'
		self.basic = "subscribe"
		self.jsondata = {}
