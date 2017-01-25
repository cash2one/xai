

from xai.brain.wordbase.verbs._recommend import _RECOMMEND

#calss header
class _RECOMMENDED(_RECOMMEND, ):
	def __init__(self,): 
		_RECOMMEND.__init__(self)
		self.name = "RECOMMENDED"
		self.specie = 'verbs'
		self.basic = "recommend"
		self.jsondata = {}
