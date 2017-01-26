

from xai.brain.wordbase.nouns._harm import _HARM

#calss header
class _HARMED(_HARM, ):
	def __init__(self,): 
		_HARM.__init__(self)
		self.name = "HARMED"
		self.specie = 'nouns'
		self.basic = "harm"
		self.jsondata = {}
